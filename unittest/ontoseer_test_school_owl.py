import sys
import os
import unittest


current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)
from main.ontoseer_main import *

ontology_file = "../owl_files/school_owl"

class TestOntoseer(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.ontology = Ontoseer(ontology_file)

    def test_listClassName(self):
        class_name = ['Book', 'Human_1234being', 'Person', 'Professor', 'RFID_000017', 'School', 'Student', 'non_teaching', 'staff', 'teacher', 'teaching', 'workers']
        self.assertCountEqual(self.ontology.getClassName(), class_name)

    def test_listPropertyName(self):
        property_name = ['roll_number', 'admits']
        self.assertCountEqual(self.ontology.getPropertyName(), property_name)

    def test_ClassNameRecommendation(self):
        self.assertEqual(self.ontology.getClassNameRecommendation('Human_1234being'), ['human1234being'])
        self.assertEqual(self.ontology.getClassNameRecommendation('Human_1234being_1'), [])
        self.assertEqual(self.ontology.getClassNameRecommendation('RFID_000017'), ['rfid000017'])

    def test_PropertyNameRecommendation(self):
        self.assertEqual(self.ontology.getPropertyNameRecommendation('roll_number'), ['rollNumber'])
        self.assertEqual(self.ontology.getPropertyNameRecommendation('Human_1234being_1'), [])
        self.assertEqual(self.ontology.getPropertyNameRecommendation('admits'), ['admits'])
    
    def test_VocabRecommendation(self):
        self.assertCountEqual(self.ontology.getVocabRecommendation('Book'), ['comicbookontology', 'BIBFRAME', 'Linked Earth landing'])
        self.assertCountEqual(self.ontology.getVocabRecommendation('Person'), ['foaf', 'Persoon', 'Sport Ontology', 'The Data Knowledge Vocabulary', 'DBpedia', 'BIBFRAME', 'Linked Earth landing', 'Cedric-cnam', 'Occupancy Profile ontology'])
        self.assertCountEqual(self.ontology.getVocabRecommendation('fdafdfa'), [])

    def test_AxiomRecommendation(self):
        self.assertCountEqual(self.ontology.getAxiomRecommendation('Person'), [('Person  subclassof  Agent', 0.8480000000000001), ('Person  subclassof  Person', 0.8461538461538461), ('Person  subclassof  Contact', 0.8444444444444446)])
        self.assertCountEqual(self.ontology.getAxiomRecommendation('Book'), [('Book  subclassof  Book', 0.8363636363636363), ('Book  subclassof  Text', 0.8363636363636363), ('Book  subclassof  Publication', 0.8275862068965518)])

    def test_OntologyDesignPattern(self):
        self.assertCountEqual(self.ontology.getOntologyDesignPattern("College", ["College", "", ""]), [['ConceptGroup',  'http://sites.google.com/site/pierreyvesvandenbussche/resources/ConceptGroup.owl'], ['Collection',  'http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl'], ['ObjectRole', 'http://ontologydesignpatterns.org/cp/owl/objectrole.owl']])
        self.assertCountEqual(self.ontology.getOntologyDesignPattern("Book,Professor,School,Student", ["College", "", ""]), [['ConceptGroup',  'http://sites.google.com/site/pierreyvesvandenbussche/resources/ConceptGroup.owl'], ['ConceptTerms',  'http://sites.google.com/site/pierreyvesvandenbussche/resources/ConceptTerms.owl'], ['TimeIndexedClassification','http://www.ontologydesignpatterns.org/cp/owl/timeindexedclassification.owl']])

    def test_ClassHierarchyValidation(self):
        self.assertCountEqual(self.ontology.getClassHierarchyValidation(["y", "n", "y" ,"n"]), ['Rigidity is correctly maintained', 'Identity is correctly maintained', 'Unity is not correctly maintained. Subclass hierarchy is not correct'])
        self.assertCountEqual(self.ontology.getClassHierarchyValidation(["n", "y", "y" ,"n"]), ['Rigidity is not correctly maintained. Subclass hierarchy is not correct', 'Identity is correctly maintained', 'Unity is not correctly maintained. Subclass hierarchy is not correct'])


if __name__ == "__main__":
    unittest.main()