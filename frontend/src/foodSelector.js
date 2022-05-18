import './App.css';

function FoodSelector(props) {
  return (
    <select>
      {props.items.map(item => <option>{item}</option>)}
    </select>
  )
}

export default FoodSelector;