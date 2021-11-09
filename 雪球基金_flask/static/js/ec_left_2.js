var ec_center =echarts.init(document.getElementById('l2'));
var option = {
    title: {
        text: '消费者的年龄分布',
        subtext: '数据来自网络'
    },
    tooltip: {
    },
    legend: {
        data: [ '2020年']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    xAxis: [{
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    {
        type: "value",
        name: "万"
    }],
    yAxis: {
        type: 'category',
        data: ['24岁以下', '24岁-30岁', '31岁-35岁', '36岁-40岁', '40岁-50岁', '50岁以上']
    },
    series: [
        {
            name: '2020年',
            type: 'bar',
            color: '#4962FC',
            data: [11.3243, 30.3438, 70.1478, 62.1594, 32.4141, 8.1807]
        }
    ]
};
        ec_center.setOption(option);