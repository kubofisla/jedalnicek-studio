import './plan.css'
import React from 'react'
import { useState, useEffect } from 'react'
import MealPicker from './mealPicker'
import ShoppingList from './shoppingList'

function Plan() {
    const periodValues = ["Pondelok", "Utorok", "Streda", "Stvrtok", "Piatok", "Sobota", "Nedela"]
    const localValues = ["Ranajky", "Obed", "Vecera"]

    const [meals, setMeals] = useState()
    const [loaded, setLoad] = useState()
    const [groups, setGroups] = useState()
    const [actualMeals, setActualMeals] = useState(new Map(loadActualMealsFromSession()))

    function loadActualMealsFromSession() {
        return getAllId().map(key => [key, getMealId(key)])
    }

    function getMealId(key) {
        let meal = JSON.parse(sessionStorage.getItem(key))

        if (meal == undefined) {
            return 0
        }

        return meal.value
    }

    useEffect(() => {
        fetch("/plan").then(
            response => response.json()
        ).then(
            response => {
                const fields = response
                console.log(fields)
                setGroups(fields)
            }
        ).catch(error => console.log(error))

        fetch("/meals").then(
            response => response.json()
        ).then(
            response => {
                const recipes = [{value: 0, label: "Nic"}]
                response.forEach(recipe => recipes.push({ value: recipe.id, label: `${recipe.name} #${recipe.type}` }))
                console.log(recipes)
                setMeals(recipes)
                setLoad(true)
            }
        ).catch(error => console.log(error))
    }, [])


    function handleMealChange(id, value) {
        actualMeals.set(id, value.value)
        setActualMeals(actualMeals)
        console.log(actualMeals)
    }

    function getAllId()
    {
        let output = []
        periodValues.forEach(period => {
            localValues.forEach(local => output.push(`${period}.${local}`))
        });
        return output
    }

    if (loaded != true)
    {
        return <div>Loading...</div>
    }

    return (
        <div className='block'>
            <div className='mainBlock'>
                {groups.map(group =>
                    <div className='period'>
                        <h3 className="column">{group.name}</h3>
                        <div className="main">
                        {group.inputs.map(select => {
                            const id = group.name + "." + select.name
                            return(
                                <div>
                                    {select.name}
                                    <MealPicker
                                        id={id}
                                        recipes={meals}
                                        default={JSON.parse(sessionStorage.getItem(id))}
                                        onChange={handleMealChange.bind(this)} />
                                </div>)
                        })}
                        </div>
                    </div>
                )}
            </div>
            <div className='toolsBlock'>
                <ShoppingList mealsMap={actualMeals}/>
            </div>
        </div>
    )
}

export default Plan