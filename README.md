# Ontoseer-Api

A Python API of OntoSeer, It is standalone class based version of Ontoseer plugin used in Protegé


## Getting Started

Use this repo as package and use all feature from class as module and function.

### Installation

1. Clone the repo

    ```sh
   git clone https://github.com/kracr/ontoseer-api
   ```

2. Create conda or venv environment with python>=3.10

3. Install packages

   ```sh
   pip install -r requirements.txt
   ```

### File stucture

```
ontoseer_api/
├─ main/
│  ├─ ontoseer_main.py
│  ├─ repository/
│     ├─ axiom_recommendation_list.py
│     ├─ odp_list.py
│     ├─ vocab_recommendation.py
├─ owl_files/
├─ unittest/
├─ .gitignore
├─ README.md
```

## Usage

* Import repo as packing in python file.

    ```sh
    from ontoseer_api.main import Ontoseer
    ```

* Initialise object with ontology filename, filename can be relative

    ```sh
    obj = Ontoseer("example_ontology.owl")
    ```

* With the obj use function related to ontology file, for example

    ```sh
    obj.getClassName()
    obj.getPropertyName()
    ```

## Class and functions

class ontoseer take filename to initialize obj and it contain following methods

- **getClassName() -> list[str]**   
    List all class name present in the ontology file.

- **getPropertyName() -> list[str]**    
    List all property name present in the ontology file

- **getClassNameRecommendation(name: str) -> list[str]**    
    Naming convention for class name in ontology file


- **getPropertyNameRecommendation(name: str) -> list[str]** 
    Naming convention for property name in ontology file

- **getVocabRecommendation(self, name: str) -> list[str]**  
    Search vocab from vocab repository


- **getAxiomRecommendation(self, name: str) -> list[str]**  
    Axiom recommendation from class or property from owl file


- **getOntologyDesignPattern(self, class_name: str, answers: list[str]) -> list[str]**  
    Ontology design validation from class or property from owl file

    - class_name: If it none then classes from ontology file wiil be used.
    - answer: answer will be always of 3 length where each element should be of str type, "" will be treated as None and each element represant following with order:   
        1. Description of ontology.
        2. Domain of ontology.
        3. Compepentancy questions related to it.

- **getClassHierarchyValidation(self, answers: list[str]) -> list[str]**
    Class hierarchy validation from class or property from owl file

    - answer: answer will be always of 4 length where each element should be of str type with choice either 'y' or 'n', each element represent following question with following order: 
        1. Do the properties of superclass cease to exist in the future (temporal dependency)?    
        2. Do the properties of the sub class cease to exist in the future? (temporal dependency)?
        3. Are the properties of super-class and subclass identical?
        4. Are the properties of subclass part of the properties whole class?