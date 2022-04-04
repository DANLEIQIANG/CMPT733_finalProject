import React, { Component } from "react";
import * as echarts from "echarts";
import { PropTypes } from "prop-types";
import { debounce } from "../utils";

export default class LineChart extends Component {
    static propTypes = {
        width: PropTypes.string,
        height: PropTypes.string,
        className: PropTypes.string,
        styles: PropTypes.object,
    };
    static defaultProps = {
        width: "100%",
        height: "350px",
        styles: {},
        className: "",
    };
    state = {
        chart: null,
        country : this.props.country,
        positive_coutry : this.props.positive_coutry,
        negative_country : this.props.negative_country,
        neutral_country : this.props.neutral_country
    };

    componentDidMount() {
        debounce(this.initChart.bind(this), 300)();
        window.addEventListener("resize", () => this.resize());
    }
    componentWillReceiveProps(nextProps) {
        if (nextProps.sidebarCollapsed !== this.props.sidebarCollapsed) {
            this.resize();
        }
        if (nextProps.chartData !== this.props.chartData) {
            debounce(this.initChart.bind(this), 300)();
        }
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
        const animationDuration = 3000;
        this.state.chart.setOption({
            backgroundColor: "#fff",
            xAxis: {
                data: this.props.country,
                boundaryGap: false,
                axisTick: {
                    show: false,
                },
            },
            grid: {
                left: 10,
                right: 10,
                bottom: 10,
                top: 30,
                containLabel: true,
            },
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    type: "cross",
                },
                padding: [5, 10],
            },
            yAxis: {
                axisTick: {
                    show: false,
                },
            },
            legend: {
                data: ["Negative","Positive","Neutral"],
            },
            series: [
                {
                    name: "Negative",
                    itemStyle: {
                        normal: {
                            color: "#FF005A",
                            lineStyle: {
                                color: "#FF005A",
                                width: 2,
                            },
                            areaStyle: {
                                color: "#f8dee2",
                            },
                        },
                    },
                    smooth: true,
                    type: "line",
                    data: this.props.negative_country,
                    animationDuration: 2800,
                    animationEasing: "cubicInOut",
                },
                {
                    name: "Positive",
                    smooth: true,
                    type: "line",
                    itemStyle: {
                        normal: {
                            color: "#3dc779",
                            lineStyle: {
                                color: "#3dc779",
                                width: 2,
                            },
                            areaStyle: {
                                color: "#f5f8f2",
                            },
                        },
                    },
                    data: this.props.positive_coutry,
                    animationDuration: 2800,
                    animationEasing: "quadraticOut",
                },
                {
                    name: "Neutral",
                    smooth: true,
                    type: "line",
                    itemStyle: {
                        normal: {
                            color: "#c4b531",
                            lineStyle: {
                                color: "#c4b531",
                                width: 2,
                            },
                            areaStyle: {
                                color: "#fafaf9",
                            },
                        },
                    },
                    data: this.props.neutral_country,
                    animationDuration: 2800,
                    animationEasing: "quadraticOut",
                },
            ],
        });
    }

    initChart() {
        if (!this.el) return;
        this.setState({ chart: echarts.init(this.el,"macarons") }, () => {
            this.setOptions(this.props.chartData);
        });
    }

    render() {
        const { className, height, width,styles } = this.props;
        debounce(this.setOptions.bind(this), 300)();
        return (
            <div
                className={className}
                ref={(el) => (this.el = el)}
                style={{
                    ...styles,
                    height,
                    width,
                }}
            />
        );
    }
}
