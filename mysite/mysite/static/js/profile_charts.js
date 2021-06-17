var ctxy = document.querySelectorAll('canvas');
for(var i=0; i<ctxy.length; i++){
var ctx=ctxy[i].getContext('2d');
ctx.canvas.style.width = 10 + "px";
ctx.canvas.style.height = 10 + "px";
var data1 = ctxy[i].id;
var data2 = 100 - ctxy[i].id;
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        datasets: [{
            data: [data1, data2],
            backgroundColor: [
                'rgba(25, 25, 112, 0.2)',
                'rgba(255, 255, 255, 0.2)'
            ]
        }]
    },
    options: {
    plugins: {
      legend: false,
      tooltip: false,
    },
    responsive: true,
    maintainAspectRatio: false,

  },
});
}