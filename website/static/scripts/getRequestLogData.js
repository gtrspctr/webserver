var apiUrl = 'api/requests';

var gotData = null;
var sortDirection = true;
var sortedColumn = null;

fetchDataAndInject();

async function fetchDataAndInject() {
    try {
        await getRequestLogData();
        console.log("Data: ", gotData);
        injectRequestLogData(gotData);
    } catch (error) {
        console.error('Error: ', error);
    }
}

async function getRequestLogData() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        gotData = data;

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
        });

    } catch (error) {
        throw error;
    }
}

function injectRequestLogData(data) {
    const request_log_TableBody = document.getElementById('request_log_TableBody')
    let dataHtml = '';

    for (var line in data) {
        dataHtml += `<tr>
                        <td>${data[line].ip}</td>
                        <td>${data[line].isp}</td>
                        <td>${data[line].city}</td>
                        <td>${data[line].country}</td>
                        <td>${data[line].method}</td>
                        <td>${data[line].agent}</td>
                        <td>${data[line].created_at}</td>
                    </tr>`;
        
    }
    request_log_TableBody.innerHTML = dataHtml;
}

function sortColumn(column) {
    var dataType = typeof Object.values(gotData)[0][column];
    console.log("Type: ", dataType);
    console.log(column)

    if (sortedColumn === column) {
        sortDirection = !sortDirection;
    } else {
        sortDirection = true;
        sortedColumn = column;
    }
    
    sortedData = gotData.sort(function (a, b) {
        var valueA = a[column];
        var valueB = b[column];

        return sortDirection
            ? valueA.localeCompare(valueB, undefined, { sensitivity: 'base' })
            : valueB.localeCompare(valueA, undefined, { sensitivity: 'base' })
    })

    injectRequestLogData(sortedData)
}