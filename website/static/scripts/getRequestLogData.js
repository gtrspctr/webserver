var apiUrl = 'api/requests';

var gotData = null;
var sortDirection = true;
var sortedColumn = null;

var currentPage = 1;
var pageSize = 10; // Number of rows per page
var totalRows = 0;
var totalPages = 0;

fetchDataAndInject();

async function fetchDataAndInject() {
    try {
        await getRequestLogData();
        console.log("Data: ", gotData);
        //injectRequestLogData(gotData);
        totalRows = gotData.length;
        totalPages = Math.ceil(totalRows / pageSize);
        renderPagination();
        renderTableData(currentPage);
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
            /*
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
            }*/
            if (entry.agent.includes("/Command/Base64/")) {
                entry.agent = "[REDACTED]"
            }
        });

    } catch (error) {
        throw error;
    }
}

function renderTableData(page) {
    const start = (page -1) * pageSize;
    const end = start + pageSize;
    const pageData = gotData.slice(start, end);
    injectRequestLogData(pageData);
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

function renderPagination() {
    const paginationContainer = document.getElementById('pagination-container');
    let paginationHtml = '';

    // Calculate the number of pages to show before and after the current page
    const numPagesToShow = 5;
    let startPage = Math.max(1, currentPage - Math.floor(numPagesToShow / 2));
    let endPage = Math.min(totalPages, startPage + numPagesToShow - 1);

    const pagesToShow = endPage - startPage + 1;
    if (pagesToShow < numPagesToShow) {
        if (startPage === 1) {
            endPage = Math.min(totalPages, startPage + numPagesToShow - 1);
        } else if (endPage === totalPages) {
            startPage = Math.max(1, endPage - numPagesToShow + 1);
        }
    }

    // Adjust startPage again if necessary
    startPage = Math.max(1, endPage - numPagesToShow + 1);

    // Start Button
    paginationHtml += `<button onclick="goToPage(1)" ${currentPage === 1 ? 'disabled' : ''}>First</button>`;

    // Number Buttons
    for (let i = startPage; i <= endPage; i++) {
        paginationHtml += `<button onclick="goToPage(${i})" ${currentPage === i ? 'disabled' : ''}>${i}</button>`;
    }

    // Last Button
    paginationHtml += `<button onclick="goToPage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''}>Last</button>`;

    paginationContainer.innerHTML = paginationHtml;
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

    // Store the current page before sorting
    const currentPageBeforeSort = currentPage;

    // Sort the entire dataset
    sortedData = gotData.sort(function (a, b) {
        var valueA = a[column];
        var valueB = b[column];

        return sortDirection
            ? valueA.localeCompare(valueB, undefined, { sensitivity: 'base' })
            : valueB.localeCompare(valueA, undefined, { sensitivity: 'base' })
    });

    // Render the table data for the current page after sorting
    renderTableData(currentPageBeforeSort);
}

function goToPage(page) {
    currentPage = page;
    renderTableData(currentPage);
    renderPagination();
}