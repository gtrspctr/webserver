var myArray = [
    {'count': '10', 'ip': '1.1.1.1', 'location': 'USA', 'method': 'GET', 'agent': 'Chrome'},
    {'count': '9', 'ip': '9.9.9.9', 'location': 'Russia', 'method': 'HEAD', 'agent': 'curl'},
    {'count': '7', 'ip': '102.21.2.33', 'location': 'China', 'method': 'GET', 'agent': 'iPhone'}
]

var apiUrl = 'api/requests'
var geoIpUrlPrefix = 'https://api.geoiplookup.net/?query='
var geoIpUrlSuffix = '&json=true'

getRequestCountryCode()
getTableData()

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

function getTableData() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            var ipData = {};

            data.forEach(entry => {
                // Parse agent and replace with smaller description
                //var agent_type = entry.ip;
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

            var table = document.getElementById('myTable')
            for (var ip in ipData) {
                if (ipData.hasOwnProperty(ip)) {
                    var row = `<tr>
                               <td>${ipData[ip].count}</td>
                               <td>${ip}</td>
                               <td>${ipData[ip].location}</td>
                               <td>${ipData[ip].method}</td>
                               <td>${ipData[ip].agent}</td>
                           </tr>`;
                    table.innerHTML += row;
                }
            }
        })
        .catch(error => {
            console.error('Error fetching data: ', error)
        })
}
