import React, { Component } from "react";
import { Progress } from "antd";
import './index.css'
export default class BoxCard extends Component {
    state = {
        classItems : this.props.classItems
    };
    render() {
        const {classItems} = this.props
        return (
            <div className="box-card-component">
                <div style={{ position: 'relative',paddingTop:"5px" }}>
                    {classItems.map((classItem)=>{
                        return (
                            <div className="progress-item">
                                <span>{classItem.name}</span>
                                <Progress percent={classItem.percent} />
                            </div>
                        )
                    })}
                </div>

            </div>
        );
    }
}
