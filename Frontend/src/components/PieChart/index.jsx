import React, { Component } from "react";
import { PropTypes } from "prop-types";
import * as echarts from "echarts";
import { debounce } from "../utils";

export default  class PieChart extends Component {
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
        typeClass: this.props.typeClass,
        numClass: this.props.numClass,
        infoClass : this.props.infoClass,
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
                trigger: "item",
                formatter: "{a} <br/>{b} : {c} ({d}%)",
            },
            legend: {
                left: "center",
                bottom: "10",
                data: this.props.typeClass,
            },
            calculable: true,
            series: [
                {
                    name: "Info:",
                    type: "pie",
                    roseType: "radius",
                    radius: [15, 95],
                    center: ["50%", "38%"],
                    data: this.props.infoClass,
                    animationEasing: "cubicInOut",
                    animationDuration
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
        console.log("@@@"+this.state.infoClass)
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
