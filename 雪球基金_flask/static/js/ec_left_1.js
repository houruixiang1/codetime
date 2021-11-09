var ec_center =echarts.init(document.getElementById('l1'));
var option = {
     title: {
        text: '汽车销售类型分布',
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        top: '8%',
        left: 'center'
    },
    series: [
        {
            name: '访问来源',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
            },
            label: {
                show: false,
                position: 'center'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '40',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            data: [
                {value: 3104845, name: '轿车'},
                {value: 2024735, name: 'SUV'},
                {value: 514480, name: '货车'},
                {value: 843243, name: '面包车'},
                {value: 743630, name: '其他'}
            ]
        }
    ]
};
        ec_center.setOption(option);