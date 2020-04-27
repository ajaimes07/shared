var tableData; 
var tbody = d3.select("tbody");

tableData.forEach(function(meteomatics){
    var row = tbody.append("tr");
    Object.entries(meteomatics).forEach(function ([key, value]){
        console.log(key,value);
        var cell = row.append("td");
        cell.text(value);
    });
});

var button = d3.select("filter-btn");
button.on("cliick", function() {
    tbody.html("");
    var filteredData = tableData
    var inputDate = d3.select("#datetime");
    var inputValue = inputDate.property("value");
    console.log(inputValue);

    var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);

    tbody = d3.select("tbody");

    filteredData.forEach(function(daily){
        var row = tbody.append("tr");
        Object.entries(daily).forEach(function ([key,value]){
            console.log(key,value);
            var cell = row.append("td");
            cell.text(value);
        });
    });
})