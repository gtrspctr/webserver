var apiUrl = 'api/requests';  // Local URL for getting the data from the db

var gotData = null;
var sortDirection = true;
var sortedColumn = null;

// Table pagination settings
var currentPage = 1;    // Which page does the table start on
var pageSize = 25;      // How many entries are on each page
var totalRows = 0;      // How many entries in total. Calculate later
var totalPages = 0;     // How many pages in total. Calculate later

fetchDataAndInject();

async function fetchDataAndInject() {
    // Get the requested data and calculate pagination settings
    try {
        await getRequestLogData();
        //console.log("Data: ", gotData);
        totalRows = gotData.length;
        totalPages = Math.ceil(totalRows / pageSize);
        renderPagination();
        renderTableData(currentPage);
    } catch (error) {
        console.error('Error: ', error);
    }
}

async function getRequestLogData() {
    // Request data from API as json
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        gotData = data;

        // Replace any entry that includes Base64 commands because
        // they are too long and screw up the table format!
        data.forEach(entry => {
            if (entry.agent.includes("/Command/Base64/")) {
                entry.agent = "[REDACTED]"
            }
        });
    } catch (error) {
        throw error;
    }
}

function renderTableData(page) {
    // 
    const start = (page - 1) * pageSize;
    const end = start + pageSize;
    const pageData = gotData.slice(start, end);
    injectRequestLogData(pageData);
}

function injectRequestLogData(data) {
    // Inject data as HTML into the table
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
    // Configure page buttons so the user can navigate through the table
    const paginationContainer = document.getElementById('pagination-container');
    let paginationHtml = '';

    // Calculate the number of pages to show before and after the current page
    const numPagesToShow = 5;  // How many page buttons should be visible at a time
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

    // Inject HTML. Runs the goToPage() function to go to the page number the user clicks
    paginationContainer.innerHTML = paginationHtml;
}

function sortColumn(column) {
    // Sorts data alphabetically based on which column is clicked
    // Everything returned is a string, so don't need to worry about other types
    var dataType = typeof Object.values(gotData)[0][column];
    //console.log("Type: ", dataType);
    //console.log(column)

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
    // Go to the page number that was clicked and inject the appropriate data.
    // Rerun the renderPagination() function in order to refresh the page numbers.
    currentPage = page;
    renderTableData(currentPage);
    renderPagination();
}