import { Recipe } from './types';

// Helper to ensure we have valid related IDs
export const RECIPES: Recipe[] = [
  {
    id: 1,
    title: {
      en: "Avocado Toast with Poached Egg",
      sk: "Avokádový toast s pošírovaným vajcom"
    },
    image: "https://picsum.photos/id/1080/600/400",
    tags: {
      en: ["Breakfast", "Vegetarian", "Quick"],
      sk: ["Raňajky", "Vegetariánske", "Rýchle"]
    },
    ingredients: {
      en: ["2 slices Sourdough bread", "1 Ripe Avocado", "2 Eggs", "Chili flakes", "Lemon juice"],
      sk: ["2 krajce kváskového chleba", "1 zrelé avokádo", "2 vajcia", "Čili vločky", "Citrónová šťava"]
    },
    instructions: {
      en: [
        "Toast the sourdough bread until golden.",
        "Mash avocado with lemon juice, salt, and pepper.",
        "Poach eggs in simmering water for 3 minutes.",
        "Spread avocado on toast, top with egg, and sprinkle chili flakes."
      ],
      sk: [
        "Opečte chlieb dozlatista.",
        "Roztlačte avokádo s citrónovou šťavou, soľou a korením.",
        "Vajcia pošírujte vo vriacej vode 3 minúty.",
        "Natrite avokádo na toast, pridajte vajce a posypte čili vločkami."
      ]
    },
    relatedRecipeIds: [2, 7],
    calories: 350,
    protein: 13,
    carbs: 25,
    fat: 22,
    prepTime: 10,
    defaultPortions: 1
  },
  {
    id: 2,
    title: {
      en: "Berry & Yogurt Parfait",
      sk: "Jogurtový parfait s lesným ovocím"
    },
    image: "https://picsum.photos/id/429/600/400",
    tags: {
      en: ["Breakfast", "Vegetarian", "Healthy"],
      sk: ["Raňajky", "Vegetariánske", "Zdravé"]
    },
    ingredients: {
      en: ["1 cup Greek Yogurt", "1/2 cup Granola", "1/2 cup Mixed Berries", "Honey"],
      sk: ["1 šálka gréckeho jogurtu", "1/2 šálky granoly", "1/2 šálky lesného ovocia", "Med"]
    },
    instructions: {
      en: [
        "Layer yogurt at the bottom of a glass.",
        "Add a layer of granola.",
        "Top with fresh berries.",
        "Drizzle with honey before serving."
      ],
      sk: [
        "Na dno pohára dajte vrstvu jogurtu.",
        "Pridajte vrstvu granoly.",
        "Ozdobte čerstvým ovocím.",
        "Pred podávaním pokvapkajte medom."
      ]
    },
    relatedRecipeIds: [1],
    calories: 280,
    protein: 12,
    carbs: 45,
    fat: 6,
    prepTime: 5,
    defaultPortions: 1
  },
  {
    id: 3,
    title: {
      en: "Grilled Chicken Caesar Salad",
      sk: "Grilovaný kurací Caesar šalát"
    },
    image: "https://picsum.photos/id/493/600/400",
    tags: {
      en: ["Lunch", "High Protein"],
      sk: ["Obed", "Vysoký proteín"]
    },
    ingredients: {
      en: ["1 Chicken Breast", "Romaine Lettuce", "Croutons", "Parmesan Cheese", "Caesar Dressing"],
      sk: ["1 kuracie prsia", "Rímsky šalát", "Krutóny", "Parmezán", "Caesar dresing"]
    },
    instructions: {
      en: [
        "Grill chicken breast until cooked through, then slice.",
        "Chop lettuce and place in a large bowl.",
        "Toss lettuce with dressing, croutons, and parmesan.",
        "Top with sliced chicken."
      ],
      sk: [
        "Kuracie prsia ugrilujte a nakrájajte.",
        "Nakrájajte šalát a dajte do veľkej misy.",
        "Premiešajte šalát s dresingom, krutónmi a parmezánom.",
        "Navrch pridajte nakrájané kuracie mäso."
      ]
    },
    relatedRecipeIds: [4, 6],
    calories: 450,
    protein: 40,
    carbs: 15,
    fat: 25,
    prepTime: 20,
    defaultPortions: 1
  },
  {
    id: 4,
    title: {
      en: "Quinoa Veggie Bowl",
      sk: "Quinoa miska so zeleninou"
    },
    image: "https://picsum.photos/id/292/600/400",
    tags: {
      en: ["Lunch", "Vegan", "Healthy"],
      sk: ["Obed", "Vegánske", "Zdravé"]
    },
    ingredients: {
      en: ["1 cup Cooked Quinoa", "Roasted Chickpeas", "Cucumber", "Cherry Tomatoes", "Tahini Dressing"],
      sk: ["1 šálka uvarenej quinoy", "Pečený cícer", "Uhorka", "Cherry paradajky", "Tahini dresing"]
    },
    instructions: {
      en: [
        "Arrange quinoa in a bowl.",
        "Add roasted chickpeas and chopped vegetables.",
        "Drizzle generously with tahini dressing.",
        "Mix well and enjoy."
      ],
      sk: [
        "Do misky dajte quinou.",
        "Pridajte pečený cícer a nakrájanú zeleninu.",
        "Bohato polejte tahini dresingom.",
        "Dobre premiešajte a podávajte."
      ]
    },
    relatedRecipeIds: [3, 8],
    calories: 400,
    protein: 14,
    carbs: 48,
    fat: 16,
    prepTime: 15,
    defaultPortions: 1
  },
  {
    id: 5,
    title: {
      en: "Lemon Herb Salmon",
      sk: "Losos na bylinkách a citróne"
    },
    image: "https://picsum.photos/id/108/600/400",
    tags: {
      en: ["Dinner", "Pescatarian", "Healthy"],
      sk: ["Večera", "Pescatariánske", "Zdravé"]
    },
    ingredients: {
      en: ["Salmon Fillet", "Lemon slices", "Fresh Dill", "Asparagus", "Olive Oil"],
      sk: ["Filet z lososa", "Plátky citróna", "Čerstvý kôpor", "Špargľa", "Olivový olej"]
    },
    instructions: {
      en: [
        "Preheat oven to 375°F (190°C).",
        "Place salmon on foil, top with lemon, dill, and oil.",
        "Arrange asparagus around salmon.",
        "Bake for 15-20 minutes until salmon flakes easily."
      ],
      sk: [
        "Predhrejte rúru na 190°C.",
        "Lososa položte na alobal, pridajte citrón, kôpor a olej.",
        "Okolo lososa rozložte špargľu.",
        "Pečte 15-20 minút."
      ]
    },
    relatedRecipeIds: [3, 9],
    calories: 500,
    protein: 35,
    carbs: 5,
    fat: 32,
    prepTime: 25,
    defaultPortions: 2
  },
  {
    id: 6,
    title: {
      en: "Classic Spaghetti Bolognese",
      sk: "Klasické špagety Bolognese"
    },
    image: "https://picsum.photos/id/835/600/400",
    tags: {
      en: ["Dinner", "Comfort Food"],
      sk: ["Večera", "Klasika"]
    },
    ingredients: {
      en: ["Spaghetti", "Ground Beef", "Tomato Sauce", "Onion", "Garlic", "Italian Herbs"],
      sk: ["Špagety", "Mleté hovädzie mäso", "Paradajková omáčka", "Cibuľa", "Cesnak", "Talianske bylinky"]
    },
    instructions: {
      en: [
        "Boil water and cook spaghetti al dente.",
        "Sauté onions and garlic, then brown the beef.",
        "Add tomato sauce and herbs, simmer for 15 mins.",
        "Serve sauce over pasta with parmesan."
      ],
      sk: [
        "Uvarte špagety al dente.",
        "Orestujte cibuľu a cesnak, potom opečte mäso.",
        "Pridajte omáčku a bylinky, duste 15 minút.",
        "Podávajte s parmezánom."
      ]
    },
    relatedRecipeIds: [3],
    calories: 650,
    protein: 28,
    carbs: 75,
    fat: 22,
    prepTime: 30,
    defaultPortions: 4
  },
  {
    id: 7,
    title: {
      en: "Mushroom Risotto",
      sk: "Hubové rizoto"
    },
    image: "https://picsum.photos/id/225/600/400",
    tags: {
      en: ["Dinner", "Vegetarian", "Comfort Food"],
      sk: ["Večera", "Vegetariánske", "Klasika"]
    },
    ingredients: {
      en: ["Arborio Rice", "Mushrooms", "Vegetable Broth", "White Wine", "Butter", "Parmesan"],
      sk: ["Ryža Arborio", "Huby", "Zeleninový vývar", "Biele víno", "Maslo", "Parmezán"]
    },
    instructions: {
      en: [
        "Sauté mushrooms and set aside.",
        "Toast rice with butter, deglaze with wine.",
        "Slowly add warm broth while stirring constantly.",
        "Stir in mushrooms and cheese at the end."
      ],
      sk: [
        "Orestujte huby a odložte bokom.",
        "Opečte ryžu na masle, zalejte vínom.",
        "Pomaly prilievajte vývar za stáleho miešania.",
        "Nakoniec vmiešajte huby a syr."
      ]
    },
    relatedRecipeIds: [1, 6],
    calories: 550,
    protein: 12,
    carbs: 60,
    fat: 25,
    prepTime: 40,
    defaultPortions: 2
  },
  {
    id: 8,
    title: {
      en: "Spicy Tofu Stir-fry",
      sk: "Pikantné tofu so zeleninou"
    },
    image: "https://picsum.photos/id/674/600/400",
    tags: {
      en: ["Dinner", "Vegan", "Quick"],
      sk: ["Večera", "Vegánske", "Rýchle"]
    },
    ingredients: {
      en: ["Firm Tofu", "Broccoli", "Bell Peppers", "Soy Sauce", "Ginger", "Chili Paste"],
      sk: ["Pevné tofu", "Brokolica", "Paprika", "Sójová omáčka", "Zázvor", "Chilli pasta"]
    },
    instructions: {
      en: [
        "Press tofu and cut into cubes.",
        "Stir-fry tofu until crispy, remove from pan.",
        "Stir-fry vegetables with ginger.",
        "Combine everything with soy sauce and chili paste."
      ],
      sk: [
        "Tofu osušte a nakrájajte na kocky.",
        "Opečte tofu do chrumkava, vyberte z panvice.",
        "Orestujte zeleninu so zázvorom.",
        "Všetko zmiešajte so sójovou omáčkou a chilli."
      ]
    },
    relatedRecipeIds: [4],
    calories: 380,
    protein: 18,
    carbs: 30,
    fat: 20,
    prepTime: 15,
    defaultPortions: 2
  },
  {
    id: 9,
    title: {
      en: "Banana Oat Pancakes",
      sk: "Banánovo-ovsené lievance"
    },
    image: "https://picsum.photos/id/824/600/400",
    tags: {
      en: ["Breakfast", "Vegetarian", "Sweet"],
      sk: ["Raňajky", "Vegetariánske", "Sladké"]
    },
    ingredients: {
      en: ["2 Ripe Bananas", "2 Eggs", "1/2 cup Oats", "Cinnamon", "Maple Syrup"],
      sk: ["2 zrelé banány", "2 vajcia", "1/2 šálky ovsených vločiek", "Škorica", "Javorový sirup"]
    },
    instructions: {
      en: [
        "Blend bananas, eggs, oats, and cinnamon.",
        "Pour batter onto a hot, greased griddle.",
        "Cook until bubbles form, then flip.",
        "Serve warm with maple syrup."
      ],
      sk: [
        "Rozmixujte banány, vajcia, vločky a škoricu.",
        "Cesto lejeme na horúcu panvicu.",
        "Pečte, kým sa netvoria bublinky, potom otočte.",
        "Podávajte teplé so sirupom."
      ]
    },
    relatedRecipeIds: [2, 1],
    calories: 320,
    protein: 9,
    carbs: 52,
    fat: 8,
    prepTime: 15,
    defaultPortions: 2
  },
  {
    id: 10,
    title: {
      en: "Smoothie Bowl",
      sk: "Smoothie miska"
    },
    image: "https://picsum.photos/id/326/600/400",
    tags: {
      en: ["Breakfast", "Vegan", "Healthy"],
      sk: ["Raňajky", "Vegánske", "Zdravé"]
    },
    ingredients: {
      en: ["Frozen Banana", "Spinach", "Almond Milk", "Chia Seeds", "Coconut Flakes"],
      sk: ["Mrazený banán", "Špenát", "Mandľové mlieko", "Chia semienka", "Kokosové lupienky"]
    },
    instructions: {
      en: [
        "Blend frozen banana, spinach, and almond milk until thick.",
        "Pour into a bowl.",
        "Top with chia seeds and coconut flakes.",
        "Serve immediately."
      ],
      sk: [
        "Rozmixujte banán, špenát a mlieko do hladka.",
        "Vylejte do misky.",
        "Posypte chia semienkami a kokosom.",
        "Ihneď podávajte."
      ]
    },
    relatedRecipeIds: [2],
    calories: 250,
    protein: 4,
    carbs: 42,
    fat: 9,
    prepTime: 5,
    defaultPortions: 1
  }
];