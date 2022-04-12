import React, {Component} from 'react';
import "./index.css";
import { Row, Col,Select} from "antd";
const { Option } = Select;


function onChange(value) {
  console.log(`selected ${value}`);
}

function onSearch(val) {
  console.log('search:', val);
}

class File extends Component{

      state = {
         newValue: [],
         record: ["1"],
       }


   onChangeSelect = (value, index) => {
       const { record } = this.state;
       console.log('===============点击的value', value)
       record[index] = value || '';
       console.log('===============record', record,record.length,typeof record[0],record[0]);
       this.setState({ record: record
       });
       console.log(this.state)
     }

     onSearchSelect = (value, index) => {
       const { newValue } = this.state;
       if (!!value) {
         newValue[index] = value || '';
         this.setState({ newValue });
       }
     }

    render() {
        const { record } = this.state;

            return (

                <div >
                    <Select
                        showSearch
                        placeholder="Select the events"
                        optionFilterProp="events"
                       onChange={(e) => this.onChangeSelect(e, '0')}
                         onSearch={value => this.onSearchSelect(value, '0')}
                        filterOption={(input, option) =>
                          option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
                        }
                      >
                        <Option value="1">2016 US Election</Option>
                        <Option value="2">2020 US Election</Option>
                        <Option value="3">Russian-Ukrainian war</Option>
                        <Option value="4">Covid-19</Option>
                      </Select>
                    <div className="chart-wrapper">

                        <h2>
                        {record =='1'? '2016 US Election':'2020 US Election'}
                         </h2>
                            <Row gutter={32}>
                                <Col xs={24} sm={24} lg={12}>
                                  <div className="chart-wrapper">
                                            <img src={require("./"+record+'.png')} alt=""/>
                                    </div>
                                </Col>
                            </Row>
                            <h2 style={{whiteSpace: 'pre-wrap'}}>
                            {record =='1'? "Cluster 36 shows that people were surprised by the results:\n ['trump', 'donald', 'transit', 'pick', 'post', 'lip', 'frank', 'elect',  'jesu', '4', 'latest', 'top', 'christian', 'defens', 'indic', 'orampblkmeld', 'cut', 'elexp', '2018', 'bernie4'] \
                            Cluster 53 shows that President Clinton is frequently mentioned in comparison to Trump:\n ['trump', 'vote', 'elector', 'lead', 'popular', 'say', 'expect', 'chang', 'interest', 'cast', 'yet', 'clinton', 'minut', 'know', 'last',  'threaten', 'land1', 'way', 'prioriti', 'dark'] \n Cluster 17 we can see Russia, Putin and child vote: \n['trump', 'putin', 'snl', 'tax', 'know', 'donald', 'game', 'russia', 'partner', 'imbecil', 'putinrun', 'big', 'disqualifi', 'childvote', 'bartertown', 'man', 'littl', 'got', 'halliburton', 'master']\
":"In class 47, they are all about trump, need trump: \n ['trump', 'like', 'pay', 'someon', 'wall', 'hope', 'still', 'els', 'money', 'case', 'ashambruhhh', 'qualifiedand', 'moment', 'januari', '20', '2021ban', 'fragiltroglodyt', 'trumpfulli', 'also', 'needtrump']\n In class 39 and 17, they both have words: wear mask, we infer that the public is more concerned about Biden's policy on the Covid-19: \['biden','presid','trump','first','elector','senat','wear','mask','vote','still','talk','bidenbiden', 'american', 'countri', 'day','100', 'could', 'cabinet', 'harri', 'joe']\n In class 41, Russia, Putin and justice appear again: \n ['putin', 'biden', 'trump', 'someth', 'congratul', 'elect', 'russia', 'could', 'russian', 'meet', 'still', 'said', 'ask', 'republican',  'cabinet', 'justic', 'get', 'back', 'find', 'like']\
"}


                             </h2>





                    </div>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>

                    <br/>
                    <br/>


                </div>
            );
        }
}
export default File;