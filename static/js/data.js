
function buildPlot() {
    /* data route */
  var url = "mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0";
  d3.json(url).then(function(response) {

    console.log(response);

    var data = response;
  
      Plotly.newPlot("plot", data, layout);
    });
  }
buildPlot();
  



