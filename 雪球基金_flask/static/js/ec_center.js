var ec_center = echarts.init(document.getElementById('c2'));

var option = {
      title: {

        left: 'center'
      },
      tooltip: {//图形编辑
        trigger: 'item'//点对应数值
      },
      legend: {//
        orient: 'vertical',//布局方式
        left: 'left',
        data: ['中国股民分布图']
      },
      visualMap: {//视觉映射组件
        type: 'piecewise',
        pieces: [
          { min: 40000, max: 1000000, label: '大于等于40000人', color: '#372a28' },
          { min: 30000, max: 39999, label: '30000-39999人', color: '#4e160f' },
          { min: 20000, max: 29999, label: '20000-29999人', color: '#974236' },
          { min: 10000, max: 19999, label: '10000-19999人', color: '#ee7263' },
          { min: 1, max: 9999, label: '1-9999人', color: '#f5bba7' },
        ],
        color: ['#E0022B', '#E09107', '#A3E00B']
      },
      toolbox: {
        show: true,//显示策略
        orient: 'vertical',//布局方式
        left: 'right',//水平
        top: 'center',//垂直安放位置
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      roamController: {
        show: true,
        left: 'right',
        mapTypeControl: {
          'china': true
        }
      },
      series: [
        {
          name: '汽车购买数',
          type: 'map',
          mapType: 'china',
          roam: false,
          label: {
            show: true,
            color: 'rgb(249, 249, 249)'
          },
          data: [
            {
              name: '北京',
              value: 17005
            }, {
              name: '天津',
              value: 20348
            }, {
              name: '上海',
              value: 29691
            }, {
              name: '重庆',
              value: 16433
            }, {
              name: '河北',
              value: 9855
            }, {
              name: '河南',
              value: 7899
            }, {
              name: '云南',
              value: 3644
            }, {
              name: '辽宁',
              value: 3453
            }, {
              name: '黑龙江',
              value: 9777
            }, {
              name: '湖南',
              value: 7684
            }, {
              name: '安徽',
              value: 9184
            }, {
              name: '山东',
              value: 20327
            }, {
              name: '新疆',
              value: 3392
            }, {
              name: '江苏',
              value: 38422
            }, {
              name: '浙江',
              value: 52817
            }, {
              name: '江西',
              value: 7477
            }, {
              name: '湖北',
              value: 8655
            }, {
              name: '广西',
              value: 5433
            }, {
              name: '甘肃',
              value: 5678
            }, {
              name: '山西',
              value: 24256
            }, {
              name: '内蒙古',
              value: 2644
            }, {
              name: '陕西',
              value: 3456
            }, {
              name: '吉林',
              value: 11978
            }, {
              name: '福建',
              value: 25584
            }, {
              name: '贵州',
              value: 23533
            }, {
              name: '广东',
              value: 45093
            }, {
              name: '青海',
              value: 893
            }, {
              name: '西藏',
              value: 1417
            }, {
              name: '四川',
              value: 11053
            }, {
              name: '宁夏',
              value: 2043
            }, {
              name: '海南',
              value: 23378
            }, {
              name: '台湾',
              value: 15040
            }, {
              name: '香港',
              value: 5140
            }, {
              name: '澳门',
              value: 5000
            }
          ]
        }
      ]
    };

    //使用指定的配置项和数据显示图表
    ec_center.setOption(option);
