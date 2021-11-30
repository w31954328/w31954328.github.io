var page3_ec_l1=echarts.init(document.getElementById("chart"),"dark")
var page3_ec_l1_option = {
    backgroundColor:'#0d1117',
    title: {
        text: '累计接种剂次前十地区'
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        axisLabel: {
            interval: 0,
            rotate: 10,
            inside: false,
            textStyle: {
                fontSize:'20',
            }
        },
    },
    yAxis: {
        type: 'value',
        axisLabel: { interval: 0, rotate: 50 },
    },
    series: [{
        itemStyle: {
              normal: {
                color:"#00fff7",
              },
            },
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
    }]
};
page3_ec_l1.setOption(page3_ec_l1_option)