var myArray = [
    {'count': '10', 'ip': '1.1.1.1', 'location': 'USA', 'method': 'GET', 'agent': 'Chrome'},
    {'count': '9', 'ip': '9.9.9.9', 'location': 'Russia', 'method': 'HEAD', 'agent': 'curl'},
    {'count': '7', 'ip': '102.21.2.33', 'location': 'China', 'method': 'GET', 'agent': 'iPhone'}
]

var apiUrl = 'api/requests';
var geoIpUrlPrefix = 'https://api.geoiplookup.net/?query=';
var geoIpUrlSuffix = '&json=true';

var gotData = null;
var sortDirection = true;

//getRequestCountryCode();
fetchDataAndInject();

function getRequestCountryCode() {
    /* GOOD
        get ip
        see if it's in the table
        if so:
            get the country code
        else:
            fetch country code
            store in table
        display it to scoreboard
    */

    /*  SIMPLE
        get ip
        fetch country code
        display it to scoreboard
    */
}

async function fetchDataAndInject() {
    try {
        await getScoreboardData();
        //console.log("Data: ", gotData);
        //console.log("Fetch: ", gotData);
        injectScoreboardData(gotData);
    } catch (error) {
        console.error('Error: ', error);
    }
}

async function getScoreboardData() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        var ipData = {};

        data.forEach(entry => {
            // Parse agent and replace with smaller description
            if (entry.agent.includes("Googlebot")) {
                entry.agent = "Googlebot";
            } else if (entry.agent.includes("HeadlessChrome")) {
                entry.agent = "HeadlessChrome";
            } else if (entry.agent.includes("Android")) {
                entry.agent = "Android";
            } else if (entry.agent.includes("iPhone" )) {
                entry.agent = "iPhone";
            } else if (entry.agent.includes("iPad")) {
                entry.agent = "iPad";
            } else if (entry.agent.includes("Windows Phone")) {
                entry.agent = "Windows Phone";
            } else if (entry.agent.includes("Windows NT")) {
                entry.agent = "Windows NT";
            } else if (entry.agent.includes("CrOS")) {
                entry.agent = "Chrome OS";
            } else if (entry.agent.includes("Macintosh")) {
                entry.agent = "MacOS";
            } else if (entry.agent.includes("Ubuntu")) {
                entry.agent = "Ubuntu";
            }

            // Merge IPs into one entry and get a count of each
            var ip = entry.ip;
            if (!ipData[ip]) {
                ipData[ip] = {
                    count: 1,
                    location: entry.location,
                    method: entry.method,
                    agent: entry.agent
                };
            } else {
                ipData[ip].count += 1;
            }
        });

        gotData = ipData;
        //console.log("Get: ", gotData);

    } catch (error) {
        throw error;
    }
}

function injectScoreboardData(data) {
    const scoreboardTableBody = document.getElementById('scoreboardTableBody')
    let dataHtml = '';

    for (var ip in data) {
        if (data.hasOwnProperty(ip)) {
            /*
            var row = `<tr>
                           <td>${ipData[ip].count}</td>
                           <td>${ip}</td>
                           <td>${ipData[ip].location}</td>
                           <td>${ipData[ip].method}</td>
                           <td>${ipData[ip].agent}</td>
                       </tr>`;
            scoreboardTableBody.innerHTML += row;
            */
            dataHtml += `<tr>
                            <td>${data[ip].count}</td>
                            <td>${ip}</td>
                            <td>${data[ip].location}</td>
                            <td>${data[ip].method}</td>
                            <td>${data[ip].agent}</td>
                        </tr>`;
        }
        
    }
    //console.log(dataHtml)
    scoreboardTableBody.innerHTML = dataHtml;
}

function sortColumn(column) {
    var dataType;
    if (column.includes("ip")) {
        var gotDataKeys = Object.keys(gotData);
        dataType = typeof gotDataKeys[0];
    } else {
        var gotDataValues = Object.values(gotData);
        dataType = typeof gotDataValues[0][column];
    }
    
    //console.log("values: ", gotDataValues);
    
    //const dataType = typeof gotDataValues[0][column];
    console.log("Type: ", dataType)
    
    sortDirection = !sortDirection;

    switch(dataType) {
        case "number":
            sortNumberColumn(column);
    }
}

function sortNumberColumn(column) {
    var sortedData = Object.keys(gotData).sort((a, b) => {
        return sortDirection ? a[column] - b[column] : b[column] - a[column];
    });

    var newData = {};
    sortedData.forEach(entry => {
        newData[entry.ip] = entry;
    });

    injectScoreboardData(newData);
}

function sortStringColumn(column) {
    //
}


//console.log(gotData);