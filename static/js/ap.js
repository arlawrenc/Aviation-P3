console.log("hay")


function myGraph(chartData, labels) {
var ctx = document.getElementById('myChart1').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Monthly Performance',
            data: chartData,
            borderColor: 'green',
            backgroundColor: 'green',
        }]
    },
    options: {
        responsive: false
    }
});
}

function SeasonGraph(chartData, labels) {
    var ctx = document.getElementById('myChart2').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Seasonal Performance',
                data: chartData,
                borderColor: 'green',
                backgroundColor: 'green',
            }]
        },
        options: {
            responsive: false
        }
    });
    }

function handler(){
    var selAirport = d3.select("#airport").property("value")
    var selHour = d3.select('#hour').node().value
    var selDate = d3.select('#flightDate').property("value")
        
    console.log(selAirport, selHour, selDate)
    
    d3.json(`/predictor/${selDate}/${selHour}/${selAirport}`,function(data){
   // d3.json(`/predictor/${selDate}/${selHour}/${selAirport}`,function(data){
              document.getElementById("log").innerHTML = data
              console.log("predictor value ", data)
          })
           
    d3.json(`/monthly_graph/${selDate}/${selHour}/${selAirport}`,function(data){
        chartlabels =  ["November", "December", "January", "March", "April", "May"];
        myGraph(data, chartlabels)
        
        console.log("Graph Data: ", data)
    })

    d3.json(`/season_graph/${selDate}/${selHour}/${selAirport}`,function(data){
        chartlabels =  ["Winter", "Spring", "Summer", "Fall"];
        SeasonGraph(data, chartlabels)
        
        console.log("Graph Data: ", data)
    })
}

//d3.select("#go").on("click",function(){
//    console.log("hay2")
//})

d3.select("#go").on("click",handler)
