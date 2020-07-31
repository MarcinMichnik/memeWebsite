import React from 'react';
import axios from 'axios';
import Meme from '../components/Memes';

const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: 'https://ant.design',
    title: `ant design part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}

class MemeList extends React.Component {

    state = {
        memes: []
    }

    componentDidMount() {
        axios.get('http://localhost:8000/api/memopolis/meme')
            .then(res => {
                this.setState({
                    memes: res.data
                })
                console.log(res.data);
            })
    }
    
    render() {
        return (
            <Meme data={this.state.memes} />
        )
    }
}

export default MemeList;