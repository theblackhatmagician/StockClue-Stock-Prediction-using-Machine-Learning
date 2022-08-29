stockCharts = {
    initDashboardPageCharts: function(graphdata) 
    {

        //....Live Graph....Candlestick

        const chartProperties = {
        width:1020,
        height:280,
        timeScale:{
            timeVisible:true,
            secondsVisible:false,
        }
        }

        const applyOptions = {
            layout: {
                backgroundColor: 'transparent',
                textColor: '#696969',
                fontSize: 12,
                fontFamily: 'Calibri',
            },
            grid: {
                vertLines: {
                    color: 'rgba(128, 128, 128, 0.5)',
                    style: 1,
                    visible: true,
                },
                horzLines: {
                    color: 'rgba(128, 128, 128, 0.5)',
                    style: 1,
                    visible: true,
                },
            },
        }


        const domElement = document.getElementById("chartBig1");
        const chart = LightweightCharts.createChart(domElement,chartProperties);
        chart.applyOptions(applyOptions);
        Series = chart.addCandlestickSeries();
        Series.setData(graphdata)

        //....Prediction Graphs....LSTM,XGBoost
        //....Switch Graphs....

        $("#0").click(function() {
            chart.removeSeries(Series);
            Series = chart.addCandlestickSeries()
            Series.setData(graphdata)

        });
        
        $("#1").click(function() {
            chart.removeSeries(Series);
            Series = chart.addLineSeries();

            graph = [
                    {time: 1625024700, value: 1580.800048828125},
                    {time: 1625111100, value: 1560.4000244140625},
                    {time: 1625197500, value: 1567.800048828125},
                    {time: 1625456700, value: 1578.949951171875},
                    {time: 1625543100, value: 1562.199951171875},
                    {time: 1625629500, value: 1564.5999755859375},
                    {time: 1625715900, value: 1560.75},
                    {time: 1625802300, value: 1562.9000244140625},
                    {time: 1626061500, value: 1571.757}
                    ]

            Series.setData(graph);

        });

        $("#2").click(function() {
            chart.removeSeries(Series);
            Series = chart.addLineSeries();
            Series.setData([
                {time: 1625024700, value: 2.14603532},
                {time: 1625111100, value: 2.04285158},
                {time: 1625197500, value: 2.25216716},
                {time: 1625456700, value: 2.01160136},
                {time: 1625543100, value: 2.09886561},
                {time: 1625629500, value: 2.23035002},
                {time: 1625715900, value: 2.01572842},
                {time: 1625802300, value: 2.04108243},
                {time: 1626061500, value: 2.25286561}
            ]);


        });
    }

    
}

