import React from 'react'

const HOST = 'http://localhost:5000'

class ShoppingList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list: [],
            isLoaded: true
        }
        this.generateList = this.generateList.bind(this);
    }

    generateList() {
        this.setState(
            {
                isLoaded: false
            }
        );

        let requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([...this.props.mealsMap.values()])
        }
        console.log(`request body: ${JSON.stringify([...this.props.mealsMap.values()])}`)

        fetch(HOST + "/shoppingList", requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const itemList = data.map(item => `${item.name} ${item.quantity}${item.unit}`)
                this.setState({meals: this.state.meals, list: itemList, isLoaded: true})
            })
    }

    render() {
        if (this.state.isLoaded != true) {
            return (<button onClick={this.generateList}>Loading...</button>)
        }
        return (
            <div>
                <button onClick={this.generateList}>Generate shopping list</button>
                <ul>
                    {this.state.list.map(element => {
                        return <li>{element}</li>
                    })}
                </ul>
            </div>
        )
    }
}

export default ShoppingList