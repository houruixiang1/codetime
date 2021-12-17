var ec_center =echarts.init(document.getElementById('r2'));
var  option = {
    title: {
        text: '名家作品top4出书量',
        subtext: '数据来自网络'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['2019年', '2020年']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    yAxis: {
        type: 'category',
        data: ['《心安即是归处》', '《晚熟的人》', '《背影》', '《活着》']
    },
    series: [
        {
            name: '2011年',
            type: 'bar',
            data: [18203, 23489, 29034, 41970]
        },
        {
            name: '2012年',
            type: 'bar',
            data: [19325, 23438, 31000, 42594]
        }
    ]
};
        ec_center.setOption(option);