import React, { Component } from "react";
import * as echarts from "echarts";
import { PropTypes } from "prop-types";
import { debounce } from "../utils";

class BarChart extends Component {
    static propTypes = {
        width: PropTypes.string,
        height: PropTypes.string,
        className: PropTypes.string,
        styles: PropTypes.object,
    };
    static defaultProps = {
        width: "100%",
        height: "300px",
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
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    // 坐标轴指示器，坐标轴触发有效
                    type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
                },
            },
            grid: {
                top: 10,
                left: "2%",
                right: "2%",
                bottom: "3%",
                containLabel: true,
            },
            xAxis: [
                {
                    type: "category",
                    data: this.props.country,
                    axisTick: {
                        alignWithLabel: true,
                    },
                },
            ],
            yAxis: [
                {
                    type: "value",
                    axisTick: {
                        show: false,
                    },
                },
            ],
            series: [
                {
                    name: "negative",
                    type: "bar",
                    stack: "vistors",
                    barWidth: "60%",
                    data:this.props.negative_country,
                    animationDuration,
                },
                {
                    name: "positive",
                    type: "bar",
                    stack: "vistors",
                    barWidth: "60%",
                    data: this.props.positive_coutry,
                    animationDuration,
                },
                {
                    name: "neutral",
                    type: "bar",
                    stack: "vistors",
                    barWidth: "60%",
                    data: this.props.neutral_country,
                    animationDuration,
                },
            ],
        });
    }

    initChart() {
        if (!this.el) return;
        this.setState({ chart: echarts.init(this.el, "macarons") }, () => {
            this.setOptions(this.props.chartData);
        });
    }

    render() {
        const { className, height, width, styles } = this.props;
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

export default BarChart;