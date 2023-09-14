# Ontoseer CLI (Ontology tools)
# Using python 3.10


# Library
from owlready2 import get_ontology
import jaro
from enum import Enum

import re
import os

# repository
from .repository.vocab_recommendation_list import vocab_repository
from .repository.axiom_recommendation_list import axiom_repository
from .repository.odp_list import odp_repository



class Ontoseer:
    """
        Ontoseer class
    """
    class ontoseer_functions(Enum):
        LC = "ListClass"
        LP = "ListProperty"
        CNR = "ClassNameRecommendation"
        PNR = "PropertyNameRecommendation"
        VCB = "VocabRecommendation"
        AXM = "AxiomRecommendation"
        ODP = "OntologyDesignPattern"
        CHV = "ClassHierarchyValidation"


    def __init__(self, ontology_file: str):
        """
            Initialise Ontoseer class
        """
        self.ontology_file = ontology_file
        self.ontology_name = ontology_file.split("/")[-1].replace(".owl", "")

        self.__check_owl_file()

        self.obj = get_ontology(ontology_file).load()
        self.__list_class_name()
        self.__list_property_name()

        # parameters for AXM
        self.AXM_Top_result_rank = 3
        self.AXM_Threshold = 0.7


    def __check_owl_file(self) -> bool:
        """
            It will check if the owl file is present and owl file is workable
        """
        try:
            if not os.path.isfile(self.ontology_file):
                raise FileNotFoundError 
            get_ontology(self.ontology_file).load()
            return True

        except FileNotFoundError as e:
            print("Please check the file path and file")
            print("Error: ", e)
            return
        except Exception as e:
            print("Error occured while opening OWL file")
            print("Please check the file path and file")
            return

    def __list_class_name(self) -> None:
        """
            List class name in ontology file
        """
        ontology_classes = list(self.obj.classes())
        ontology_classes = [str(x) for x in ontology_classes]
        correct_class_name = []

        for class_name in ontology_classes:
            if class_name.startswith(self.ontology_name):
                correct_class_name.append(class_name.split(".")[-1])
        self.class_names = correct_class_name

    def __list_property_name(self) -> None:
        """
            List property name in ontology file
        """
        ontology_properties = list(self.obj.properties())
        ontology_properties = [str(x) for x in ontology_properties]
        correct_property_name = []

        for property_name in ontology_properties:
            if property_name.startswith(self.ontology_name):
                correct_property_name.append(property_name.split(".")[-1])
        self.property_names = correct_property_name


   
    # List class and property
    def getClassName(self) -> list[str]:
        return self.class_names
    
    def getPropertyName(self) -> list[str]:
        return self.property_names
    
    # Naming recommendation functions
    def __naming_convention(self, name: str) -> list[str]:
        """
        Naming convention for names in ontology file
        """
        name_suggestion = []

        # find if name contain only special character or digits
        if name.isdecimal() or re.match(r'^[^a-zA-Z0-9]*$', name):
            return ["Name contains only special character or digits, please make it alpha numeric !!!"]
        
        # if the name starts with digit or spl character or both then remove it
        if re.match(r'^[0-9\W]+', name):
            name = re.sub(r'^[0-9\W]+', '', name)
            name_suggestion.append(name)

        # remove all spl character except "_"
        if re.match(r'[\-\/@#$%^&+=()]+', name):
            name = re.sub(r'[\-\/@#$%^&+=()]+', '', name)
            name_suggestion.append(name)

        # if name contain digit in between except in the end then remove it
        if re.match(r'(?<=[a-zA-Z_])\d+(?=[a-zA-Z_])', name):
            name = re.sub(r'(?<=[a-zA-Z_])\d+(?=[a-zA-Z_])', ' ', name)
            name_suggestion.append(name)
        
        # If string contain space, tab or "_" convert it to camel case
        if ' ' in name or '\t' in name or '_' in name:
            words = re.split(r'[ _\t]', name)
            camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
            name_suggestion.append(''.join(camel_case_words))

        return name_suggestion

    def getClassNameRecommendation(self, name: str) -> list[str]:
        """
            Naming convention for class name in ontology file
        """
        if name not in self.class_names:
            print("Class name not found in the ontology file")
            return []
        else:
            names = self.__naming_convention(name)
            if names == []:
                return [name]
            return names
        
    def getPropertyNameRecommendation(self, name: str) -> list[str]:
        """
            Naming convention for property name in ontology file
        """
        if name not in self.property_names:
            print("Property name not found in the ontology file")
            return []
        else:
            names = self.__naming_convention(name)
            if names == []:
                return [name]
            return names


    # vocab recommendation functions
    def getVocabRecommendation(self, name: str) -> list[str]:
        """
            Search vocab from vocab repository
        """
        matching_ontologies = []
        for ontology_name, data in vocab_repository.items():
            classes = data[0]
            for class_name in classes:
                if name.lower() in class_name.lower():
                    matching_ontologies.append(ontology_name)
                    break
        
        if len(matching_ontologies) == 0:
            return []
        
        print(f"Vocab found in {len(matching_ontologies)} ontology(s)")
        for ontology_name in matching_ontologies:
            print(f"{ontology_name}")
            print(f"IRI   - {vocab_repository[ontology_name][2]}")
            print(f"Prefix - {vocab_repository[ontology_name][1]}")
            print("\n\n\n")

        return matching_ontologies 


    # axioms recommendation functions
    def getAxiomRecommendation(self, name: str) -> list[str]:
        """
            Axiom recommendation from class or property from owl file
        """
        scores = {}
        for axiom in axiom_repository:
            score = jaro.jaro_winkler_metric(name, axiom)
            if score >= self.AXM_Threshold:
                scores[axiom] = score
        top_result = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:self.AXM_Top_result_rank]

        return top_result


    # ontology design validation functions
    def getOntologyDesignPattern(self, class_name: str, answers: list[str]) -> list[str]:
        """
            Ontology design validation from class or property from owl file
        """
        validation_result = []

        class_property_score = []
        for ontology_name, data in odp_repository.items():
            temp_class_length = len(data[0])
            temp_class_score = []
            for name in data[0]:
                temp_class_score.append(jaro.jaro_winkler_metric(class_name, name))
            class_property_score.append(sum(temp_class_score)/temp_class_length)

        description_score = []
        for ontology_name, data in odp_repository.items():
            description_score.append(jaro.jaro_winkler_metric(answers[0], data[1]))

        domain_score = []
        for ontology_name, data in odp_repository.items():
            domain_score.append(jaro.jaro_winkler_metric(answers[1], data[1]))

        competency_score = []
        for ontology_name, data in odp_repository.items():
            competency_score.append(jaro.jaro_winkler_metric(answers[2], data[1]))

        # final score calculation
        final_score_temp = []
        for i in range(len(description_score)):
            final_score_temp.append(5*class_property_score[i] + 3*description_score[i] + 2*domain_score[i] + 3*competency_score[i])

        final_score = {}
        count = 0
        for ontology_name, data in odp_repository.items():
            final_score[ontology_name] = final_score_temp[count] 
            count += 1
        
        final_score = sorted(final_score.items(), key=lambda x: x[1], reverse=True)


        top_result = 3
        for ontology_name, score in final_score:
            validation_result.append([(ontology_name), (odp_repository[ontology_name][2])])
            if top_result == 1:
                break
            top_result -= 1

        return validation_result


    # class hierarchy validation
    def getClassHierarchyValidation(self, answers: list[str]) -> list[str]:
        """
            Class hierarchy validation from class or property from owl file
        """
        validation_result = []

        if ((answers[0] == 'y') and (answers[1] =='y' or answers[1] == 'n')):
            validation_result.append("Rigidity is correctly maintained")
        elif ((answers[0] == 'n') and (answers[1] == 'n')):
            validation_result.append("Rigidity is correctly maintained")
        elif ((answers[0] == 'n') and (answers[1] == 'y')):
            validation_result.append("Rigidity is not correctly maintained. Subclass hierarchy is not correct")

        if (answers[2] == 'y'):
            validation_result.append("Identity is correctly maintained")
        elif (answers[2] == 'n'):
            validation_result.append("Identity is not correctly maintained. Subclass hierarchy is not correct")
        
        if (answers[3] == 'y'):
            validation_result.append("Unity is correctly maintained")
        elif (answers[3] == 'n'):
            validation_result.append("Unity is not correctly maintained. Subclass hierarchy is not correct")

        return validation_result