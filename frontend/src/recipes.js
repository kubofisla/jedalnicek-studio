import "./recipes.css"
import { useEffect, useState } from 'react'

function Recipes() {
    const [recipes, setRecipes] = useState()

    useEffect(() => {
        fetch("/api/recipes").then(
            response => response.json()
        ).then(
            recipes => {
                setRecipes(recipes)
            }
        ).catch(error => console.log(error))
    }, [])


    return (
        <div>
            <h1>RECIPES</h1>
            {recipes?.map((recipe) => {
                return (
                    <div className="recipe" key={recipe.id}>
                        <h3>{recipe.name}</h3>
                        {recipe.ingredients?.map((ingredient) => {
                            return <div className="ingredient">{ingredient.quantity} {ingredient.unit} - {ingredient.ingredient}</div>
                        })}
                        <div className="description">{recipe.description}</div>
                    </div>
                )
            })}
        </div>
    )
}

export default Recipes