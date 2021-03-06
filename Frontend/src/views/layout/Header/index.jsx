import React, {Component} from 'react';
import { Layout, PageHeader } from 'antd';
import "./index.css";

const { Header} = Layout;

class MyHeader extends Component {
    render() {
        return (
            <Header className="site-layout-background" style={{ padding: 0 }}>
                <PageHeader
                    className="site-page-header"
                    title="Twitter Sentiment Analysis in Significant Events"
                />
            </Header>

        );
    }
}

export default MyHeader;