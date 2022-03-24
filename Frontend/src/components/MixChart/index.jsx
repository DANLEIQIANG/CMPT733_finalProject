import React, { Component } from "react";
import * as echarts from "echarts";
import { debounce } from "../utils";


export  default  class MixChart extends Component {
    constructor(props){
        super(props);
        this.state = {
            chart: null,
            positive : this.props.positive,
            labels: this.props.labels,
            negative: this.props.negative,
            neutral : this.props.neutral,
            overall : this.props.overall,
        };
    }

    componentDidMount() {
        debounce(this.initChart.bind(this), 300)();
        window.addEventListener("resize", () => this.resize());
    }
    componentWillReceiveProps(nextProps) {
        if (nextProps.sidebarCollapsed !== this.props.sidebarCollapsed) {
            this.resize();
        }
        this.setState({
            positive : this.props.positive,
            labels: this.props.labels,
            negative: this.props.negative,
            neutral : this.props.neutral,
            overall : this.props.overall,
        })

    }

    componentWillUnmount() {
        this.dispose();
    }


    resize() {
        const chart = this.state.chart;
        if (chart) {
            debounce(chart.resize.bind(this), 300)();
        }
    }

    dispose() {
        if (!this.state.chart) {
            return;
        }
        window.removeEventListener("resize", () => this.resize()); // 移除窗口，变化时重置图表
        this.setState({ chart: null });
    }

    setOptions() {
        const xData = (function () {
            const data = [];
            for (let i = 1; i < 13; i++) {
                data.push(i + "month");
            }
            return data;
        })();
        this.state.chart.setOption({
            backgroundColor: "rgba(146,151,154,0.06)",
            title: {
                text: "statistics",
                x: "20",
                top: "20",
                textStyle: {
                    color: "#fff",
                    fontSize: "22",
                },
                subtextStyle: {
                    color: "#90979c",
                    fontSize: "16",
                },
            },
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    textStyle: {
                        color: "#fff",
                    },
                },
            },
            grid: {
                left: "5%",
                right: "5%",
                borderWidth: 0,
                top: 150,
                bottom: 95,
                textStyle: {
                    color: "#fff",
                },
            },
            legend: {
                x: "5%",
                top: "10%",
                textStyle: {
                    color: "#90979c",
                },
                data: ["Positive", "Negative", "Neutral","Overall"],
            },
            calculable: true,
            xAxis: [
                {
                    type: "category",
                    axisLine: {
                        lineStyle: {
                            color: "#90979c",
                        },
                    },
                    splitLine: {
                        show: false,
                    },
                    axisTick: {
                        show: false,
                    },
                    splitArea: {
                        show: false,
                    },
                    axisLabel: {
                        interval: 0,
                    },
                    data: this.state.labels,
                },
            ],
            yAxis: [
                {
                    type: "value",
                    splitLine: {
                        show: false,
                    },
                    axisLine: {
                        lineStyle: {
                            color: "#90979c",
                        },
                    },
                    axisTick: {
                        show: false,
                    },
                    axisLabel: {
                        interval: 0,
                    },
                    splitArea: {
                        show: false,
                    },
                },
            ],
            dataZoom: [
                {
                    show: true,
                    height: 30,
                    xAxisIndex: [0],
                    bottom: 30,
                    start: 10,
                    end: 80,
                    handleIcon:
                        "path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z",
                    handleSize: "110%",
                    handleStyle: {
                        color: "#d3dee5",
                    },
                    textStyle: {
                        color: "#fff",
                    },
                    borderColor: "#90979c",
                },
                {
                    type: "inside",
                    show: true,
                    height: 15,
                    start: 1,
                    end: 35,
                },
            ],
            series: [
                {
                    name: "Positive",
                    type: "bar",
                    stack: "total",
                    barMaxWidth: 35,
                    barGap: "10%",
                    itemStyle: {
                        normal: {
                            color: "rgba(255,144,128,1)",
                            label: {
                                show: true,
                                textStyle: {
                                    color: "#fff",
                                },
                                position: "insideTop",
                                formatter(p) {
                                    return p.value > 0 ? p.value : "";
                                },
                            },
                        },
                    },
                    data: this.state.positive,
                },

                {
                    name: "Negative",
                    type: "bar",
                    stack: "total",
                    itemStyle: {
                        normal: {
                            color: "rgba(0,191,183,1)",
                            barBorderRadius: 0,
                            label: {
                                show: true,
                                position: "top",
                                formatter(p) {
                                    return p.value > 0 ? p.value : "";
                                },
                            },
                        },
                    },
                    data: this.state.negative,
                },
                {
                    name: "Neutral",
                    type: "bar",
                    stack: "total",
                    itemStyle: {
                        normal: {
                            color: "rgb(45,148,211)",
                            barBorderRadius: 0,
                            label: {
                                show: true,
                                position: "top",
                                formatter(p) {
                                    return p.value > 0 ? p.value : "";
                                },
                            },
                        },
                    },
                    data: this.state.neutral,
                },
                {
                    name: "Overall",
                    type: "line",
                    stack: "total",
                    symbolSize: 10,
                    symbol: "circle",
                    itemStyle: {
                        normal: {
                            color: "rgb(196,181,49)",
                            barBorderRadius: 0,
                            label: {
                                show: true,
                                position: "top",
                                formatter(p) {
                                    return p.value > 0 ? p.value : "";
                                },
                            },
                        },
                    },
                    data: this.state.overall,
                },
            ],
        });
    }



    initChart() {
        const {positive,labels,negative, neutral,overall} = this.props
        if (!this.el) return;
        this.setState({ chart: echarts.init(this.el, "macarons") }, () => {
            this.setOptions();
        });
    }

    render() {
        console.log("aaa"+this.state.friendly)
        debounce(this.setOptions.bind(this), 300)();
        return (
            <div
                style={{ width: "100%", height: "calc(90vh - 90px)" }}
                className="app-container"
            >
                <div
                    style={{ width: "100%", height: "90%" }}
                    ref={(el) => (this.el = el)}
                ></div>
            </div>
        );
    }
}
