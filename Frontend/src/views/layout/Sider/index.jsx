import React, {Component} from 'react';
import { Layout, Menu, Breadcrumb, PageHeader } from 'antd';
import {
    DesktopOutlined,
    PieChartOutlined,
    FileOutlined,
} from '@ant-design/icons';
import "./index.css";
import {Link} from "react-router-dom";
import logo from "../../../assets/SFU-block-logo.svg";

const {Sider } = Layout;
export default class SiderDemo extends React.Component {
    state = {
        collapsed: false,
    };

    onCollapse = collapsed => {
        console.log(collapsed);
        this.setState({ collapsed });
    };

    render() {
        const { collapsed } = this.state;
        return (
            <Sider collapsible collapsed={collapsed} onCollapse={this.onCollapse}>
                <div className="sidebar-logo-container">
                    <img src={logo} className="sidebar-logo" alt="logo" />
                    <h1 className="sidebar-title">Kunkun</h1>
                </div>
                <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
                    <Menu.Item key="1" icon={<PieChartOutlined />}>
                        <Link to='/overview'>Overview</Link >
                    </Menu.Item>
                    <Menu.Item key="2" icon={<DesktopOutlined />}>
                        <Link to='/analysis'>Analysis</Link >
                    </Menu.Item>
                    <Menu.Item key="3" icon={<FileOutlined />}>
                        <Link to='/file'>File</Link >
                    </Menu.Item>
                </Menu>
            </Sider>

        );
    }
}
