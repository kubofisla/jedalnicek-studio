import React from 'react'
import Select from 'react-select'
import Creatable from 'react-select/creatable';

class MealPicker extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            value: this.props.default,
        }

        this.options = this.props.recipes
    }

    createOption(inputValue) {
        let option = {value: 0, label: inputValue}
        this.handleChange(option)
    }

    handleChange(value) {
        this.setState({value: value})
        this.props.onChange(this.props.id, value)
        sessionStorage.setItem(this.props.id, JSON.stringify(value))
        console.log(`Saved meal: ${sessionStorage.getItem(this.props.id)}`)
    }

    render() {
        return (
            <Creatable
                id={this.props.id}
                className="select"
                options={this.options}
                onChange={value => this.handleChange(value)}
                onCreateOption={value => this.createOption(value)}
                value={this.state.value}
            />
        )
    }
}

export default MealPicker