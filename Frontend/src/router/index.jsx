import React from "react";
import {Breadcrumb, Layout} from "antd";
import {Route,Routes,Navigate} from 'react-router-dom'
import Sider from "../views/layout/Sider";
import Header from "../views/layout/Header";
import Overview from "../pages/Overview";
import Analysis from "../pages/Analysis";
import Cluster from "../pages/Cluster"
import File from "../pages/File";
import * as PropTypes from "prop-types";
const {Content} = Layout;

export default class MyRouter extends React.Component {
    render() {
        return (
            <Layout style={{ minHeight: '100vh' }}>
                <Sider/>
                <Layout className="site-layout">
                    <Header/>
                    <Content style={{ margin: '0 16px' }}>
                        <Breadcrumb style={{ margin: '26px 0' }}/>
                        <div className="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
                            <Routes>
                                <Route path="/overview" element={<Overview/>} />
                                <Route path="/analysis" element={<Analysis/>} />
                                <Route path="/file" element={<File/>} />
                                <Route path="/cluster" element={<Cluster/>} />
                                <Route path="/" element={<Navigate to="/overview"/>} />
                            </Routes>
                        </div>
                    </Content>
                </Layout>
            </Layout>

        );
    }
}