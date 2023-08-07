var myArray = [
    {'count': '10', 'ip': '1.1.1.1', 'location': 'USA', 'method': 'GET', 'agent': 'Chrome'},
    {'count': '9', 'ip': '9.9.9.9', 'location': 'Russia', 'method': 'HEAD', 'agent': 'curl'},
    {'count': '7', 'ip': '102.21.2.33', 'location': 'China', 'method': 'GET', 'agent': 'iPhone'}
]

buildTable(myArray)

function buildTable(data){
    var table = document.getElementById('myTable')
    for (var i = 0; i < data.length; i++){
        var row = `<tr>
                       <td>${data[i].count}</td>
                       <td>${data[i].ip}</td>
                       <td>${data[i].location}</td>
                       <td>${data[i].method}</td>
                       <td>${data[i].agent}</td>
                   </tr>`
        table.innerHTML += row
    }
}