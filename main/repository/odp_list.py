odp_repository = {  
        "ActingFor" : [
            {"actsfor","actsthrough","Agent"},
            "To represent that some agent is acting in order to forward the action of a social (non-physical) agent.",
            "http://www.ontologydesignpatterns.org/cp/owl/actingfor.owl"
        ],
        "Action" : [
            {"Action ","Action_status","has_status","is_consequence_of","is_dependent_on","Suspension","has_suspension","Performance_duration","is_duration_of","Impleented_action","is_suspension_of","plan_composed_of","Proposed_action","is_status_of","Abandoned_action","Completed_action","has_duration","action_proposed_in","has_direct_consequence","is_direct_consequence_of","is_directly_dependent_on","has_direct_dependent","has_dependent"},
            "The purpose of the pattern is to model actions that are proposed, planned, and performed or abandoned, together with their status and durations in time.",
            "http://www.ontology.se/odp/content/owl/Action.owl"
        ],
        "ActivitySpecification" : [
            {"Activity"},
            "This work is concerned with supporting a correct and meaningful representation of activities on the Semantic Web, with the potential to support tasks such as activity recognition and reasoning about causation. This requires an ontology capable of more than simply documenting and annotating individual activity occurrences; definitions of activity specifications are required. Current representations of activities in OWL do not meet the basic requirements for activity specifications. Detailed definitions of an activity's preconditions and effects are lacking, in particular with respect to a consideration of change over time. This pattern leverages existing work to fill this void with an ontology design pattern for activity specifications in OWL.",
            "http://ontology.eil.utoronto.ca/icity/ActivitySpecification"
        ],
        "AffectedBy" : [
            {"conceptualizes","executesTask","isConceptualizedBy","isExecutedIn","isParametrizedBy","isSatisfiedBy","parametrizes","satisfies","GoalSituation"},
            "Enable government and other web sites to answer an open ended collection of English questions,  and also to explain the answers in English.  Support government folks and citizens socially networking, Wikipedia-style, to continually expand the range of questions that can be answered.",
            "https://w3id.org/affectedBy"
        ],
        "AgentRole" : [
            {"FeatureOfInterest","Quality","affectedBy","belongsTo"},
            "A room (feature of interest) has a temperature (quality) and this temperature is affected by the air conditioner status, by the number of people in the room, and by the sun radiation that passes through the room’s windows",
            "http://www.ontologydesignpatterns.org/cp/owl/agentrole.owl"
        ],
        "Airline" : [
            {"Agent"},
            "To represent agents and the roles they play..",
            "http://ontologydesignpatterns.org/ekp/Airline.owl"
        ],
        "Algorithm" : [
            {"hasAircraft","Airline","Aircraft"},
            "To model algorithm specifications, their implementations and executions, together with parameters of implementations, settings of the parameters for the execution, and inputs the execution consumes (e.g., data) and outputs the execution produces (e.g., models, reports).",
            "https://github.com/ML-Schema/core/blob/master/AlgorithmImplementationExecution.owl"
        ],
        "AquaticResources" : [
            {"Algorithm","InformationEntity","Implementation","Execution","Process","ParameteSetting","Task","TimeInterval","Parameter","Input","Output","Top"},
            "To represent the encyclopedic knowledge expressed by an object typed as Airline",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/aquaticresources.owl"
        ],
        "Bag" : [
            {"AquaticSpecies","AquaticResource","WaterArea","hasSpecies","hasWaterArea","isSpeciesPresentIn","isWaterAreaOf"},
            "To represent aquatic resources or stocks as composed of aquatic organisms from one or more species, and living in a water area.",
            "http://www.ontologydesignpatterns.org/cp/owl/bag.owl"
        ],
        "BasicPlan" : [
            {"Item","itemContent","Bag","itemOf","hasItem","size"},
            "To model bags of items (elements). The Bag is characterized by a collection that can have multiple copies of each object.",
            "http://www.ontologydesignpatterns.org/cp/owl/basicplan.owl"
        ],
        "Biological Entities" : [
            {"family","group","species","order","includesOrder","includesamily","includesSpecies","Animal","Fish","Mammals","Reptiles","Birds","Person"},
            "To represent biological species and relations between them.",
            "http://www.fao.org/aims/aos/fi/species_v1.0_model.owl"
        ],
        "CatchRecord" : [
            {"countryOfRecord","fishingAreaOfRecord","forCountry","fromFishingArea","hasCatchRecord","isCatchRecordFor","unitUsedInRecord","withUnit","CatchRecord","refereneYear","amount","reportingYear","Country","UnitOfMeasure","Fish","Fishery"},
            "To represent the catch records from time series FIGIS application, which contain temporally-indexed aggregated information about aquatic species cacthing",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/catchrecord.owl"
        ],
        "Chess" : [
            {"Chess","hasmadehalfmove","hasmadequartermove"},
            "To model a flexible schema to allow exposing chess games as linked data.",
            "http://krisnadhi.github.io/onto/chesspattern.owl"
        ],
        "Classification" : [
            {"Concept","Entity","classifies","is classified"},
            "To represent the relations between concepts (roles, task, parameters) and entities (person, events, values), which concepts can be assigned to. To formalize the application (e.g. tagging) of informal knowledge organization systems such as lexica, thesauri, subject directories, folksonomies, etc., where concepts are first-order elements.",
            "http://www.ontologydesignpatterns.org/cp/owl/classification.owl"
        ],
        "ClimaticZone" : [
            {"ClimaticZone","AquaticResource","AquaticResourceObservation","hasResource","hasClimaticZon","isClimaticZoneOf","isResourceOf","hasReferenceYear"},
            "The intent of the pattern is to be able to represent climatic zones for aquatic resources.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/climaticzone.owl"
        ],
        "Collection" : [
            {"hasMember","isMemberOf","Collection"},
            "To represent domain (not set theory) membership.",
            "http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl"
        ],
        "Computer System" : [
            {"isCompatibleWith","requiresHardware","requiresSoftware","usesDriver","usesHardware","usesOperatingSystem","usesSoftware","Computer","Driver","Hardware","OperatingSystem","Softwae"},
            "The pattern intends to model computer systems based on a hardware/software approach. This pattern has been developed by MKLab at CERTH/ITI and Tate for the PERICLES FP7 project.",
            "http://mklab.iti.gr/pericles/ComputerSystem_ODP.owl"
        ],
        "Course" : [
            {"hasName","hasNumber","hasFirstName","hasLastName","taughtBy","takenBy","hasId","Course","Grad-Course","Grad-Student","Instructor","Person","Student","Under-Grad-Course","Under-Grad-tudent","hasCourseLevel","teaches","hasLevelStudent"},
            "The aim of this content ontology design patterns-Course Pattern- is to model the core attributes of a course and the basic relationships of the course in an educational institution.",
            "http://www.cs.kent.edu/~malzyoud/ODPs/Course.ow.htm"
        ],
        "Criterion" : [
            {"Criterion"},
            "The purpose of this pattern is to provide a basis for criteria modeling. For more advanced use see the 'criterion setter' pattern that enables describing entities that define criteria (such as requirements, constraints etc.).",
            "http://criteria-modeling.googlecode.com/svn/trunk/criterion.owl"
        ],
        "Persons" : [
            {"actsFor","actsThrough","introduces","isIntroducedBy","NaturlPerson","Person","SocialPerson"},
            "The relation holding between any Agent, and a SocialPerson.",
            "http://www.ontologydesignpatterns.org/cp/owl/persons.owl"
        ],
        "Price" : [
            {"hasCurrency","haPrice","isPriceOf","hasValue","Currency","Price"},
            "hasCurrency page",
            "http://www.ontologydesignpatterns.org/cp/owl/price.owl"
        ],
        "PrivacyPolicyPersonalData" : [
            {"Process","PersonalData","LawfulbasisforProcessing","DataSharingstep","uration","DataCollectionStep","CollectionMechanism","Agent","sharesData","hasDuration","haslegalbasis","hasCollectionMechanism"},
            "Provides a model for personal data information within privacy policies",
            "http://openscience.adaptcentre.ie/ontologies/privacypolicy.owl"
        ],
        "Professor" : [
            {"Professor","Univerity","Faculty"},
            "Professor building",
            "http://www.cs.kent.edu/~malzyoud/ODPs/Professsor.htm"
        ],
        "Provenance" : [
            {"Agent","ProvenanceActiviy","EntitywithProvenance"},
            "Extracted core of PROV-O",
            "https://raw.githubusercontent.com/cogan-shimizu-wsu/ProvenanceOWL/master/EntityWithProvenanceOntologyPattern.owl "
        ],
        "RelativeRelationship" : [
            {"Relationship","RelativeExistence","Entity","hasAttribute","hasScope"},
            "For dynamically conceptualizing, establishing, tracking, and updating relative relationships and dependencies between entities (real or representational) of a physical, temporal, and/or importance scope.",
            "https://curate.nd.edu/downloads/9p29086355b"
        ],
        "Reporting" : [
            {"EventReporter","ReportingEvent","ActualEvent","hasAuthor","hasContext"},
            "The intent of the pattern is to allow for modelling situations in which the knowledge about an event cannot be treated as certain. It is particularly useful for cases in which two or more agents provide different, contradictory information about the same event.",
            "http://semantic.cs.put.poznan.pl/ontologies/reportingevent.owl"
        ],
        "Set" : [
            {"Set","size "},
            "To model sets of things (elements). A Set is a collection that cannot contain duplicate elements.",
            "http://www.ontologydesignpatterns.org/cp/owl/set.owl"
        ],
        "SmartHome" : [
            {"Home","SmartHome","AirCondition","AirCondition"},
            "The SmartEnv as a network of 8 ontology patterns relies on the SSN ontology and represents a smart environment. Each pattern model one aspect of such environments including temporal, spatial, objects, network, observation etc.",
            "https://w3id.org/smartenvironment/smartenv.owl"
        ],
        "SpeciesConservation" : [
            {"AquaticSpecies","hasConservationStatus"},
            "This pattern intend to represent a description of the conservation status of aquatic species.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/speciesconservation.owl"
        ],
        "TaskExecution" : [
            {"Action","executesTask","isExecutedIn"},
            "To represent topics and their relations.",
            "http://www.ontologydesignpatterns.org/cp/owl/taskexecution.owl"
        ],
        "TimeIndexedClassification" : [
            {"TimeIndexedClassification"},
            "The pattern provides a model of trajectory, which is understood as a sequence of spatiotemporal points. The model generalizing the Semantic Trajectory pattern from [Hu, et al., COSIT 2013] by employing the notion of place, instead of location/geo-coordinate, to represent the spatial extent of the trajectory. This pattern is suitable for a variety of trajectory datasets and easily extendible by by aligning to or matching with existing trajectory ontologies, foundational ontologies, or other domain specific vocabularies.",
            "http://www.ontologydesignpatterns.org/cp/owl/timeindexedclassification.owl"
        ],
        "Time indexed person role" : [
            {"Person","TimeIndexedPersonRole"},
            "To represent basic knowledge about transitions (events, states, processes, objects).",
            "http://www.ontologydesignpatterns.org/cp/owl/timeindexedpersonrole.owl"
        ],
        "TimeInterval" : [
            {"Time Interval","has interval date","has interval start date","has interval end date"},
            "The goal of the pattern is to facilitate modelling the movement of mass or energy from one location to another, based on a common persistent frame of reference.",
            "http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl"
        ],
        "TimePeriod" : [
            {"TimePeriod","TimePeriodMeasurementUnit","hasTimePeriodeasurementUnit"},
            "To represent actions through which tasks are executed.",
            "http://www.ontologydesignpatterns.org/cp/owl/timeperiod.owl"
        ],
        "Topic" : [
            {"farTopicFrom","hasCoreConcept","hasSubTopic","hasTopic","isCoreConceptFor","isSubopicOf","isTopicOf","nearTopicTo","overlappingTopic ","Concept","Topic"},
            "A Situation to represent classification ('counting as') of an entity at some time",
            "http://ontologydesignpatterns.org/cp/owl/topic.owl"
        ],
        "Trajectory" : [
            {"atPlace","atTime","endsAt","hasAttribute","hasFix","hasSgment","hasTrajectory","nextFix","startsFrom","traversedBy","Attribute","EndingFix","Fix","MovingObject","Place","Segment","StartingFix","TimeEntity","Trajectory"},
            "To represent classification of things at a certain time.",
            "http://krisnadhi.github.io/onto/trajectory.owl"
        ],
        "VesselSpecies" : [
            {"isCaughtBy","catchesSpecies""isCaughtByVesselType"},
            "To represent time intervals.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/vesselspecies.owl"
        ],
        "Transition" : [
            {"hasEventAtTime","hasFinalStateAtTime","haInitialStateAtTime","includesFinalSituation","includesInitialSituation","includesProcess","isFinalSituationIncludedIn","isInitialSituationIncludedIn","isProcessIncludedIn","isTimeOf","occursAt","Process","Transition"},
            "To represent time periods between events.",
            "http://ontologydesignpatterns.org/cp/owl/transition.owl"
        ],
        "Transport" : [
            {"partOf","referenceFrame","transportEvent","transportEntity"},
            "To provide a direct relation between aquatic species and vessels that are able to catch them, regardless of the fishing gear used.",
            "https://wiki.auckland.ac.nz/download/attachments/52016791/TransportPattern.owl"
        ],
        "RecurrentEventSeries" : [
            {"hasImmediateNextEvent","hasNextEvent","hasImmediatePreviousEvent","Event","hasMemberEvent","hasTimePeriod","hasTimePeriodBeforeNextEvent","hasUnifyingFator","isEventMemberOf","eventNumber","Event","RecurrentEventSeries"},
            "To represent recurrent event series as situations and collections of consecutive events, with a regular time period between events and unifying factors.",
            "http://www.ontologydesignpatterns.org/cp/owl/recurrenteventseries.owl"
        ],
        "Reaction" : [
            {"directlyFollows","directlyPrecedes","hasSetting","isSettingFor","hasConsequence","hasNextAction","hasPreviousAction","hasOutcome","Action","Event","Consequence","isRaisedBy","isOutcomeOf","isCoagentWith","Situation","Reaction"},
            "To model dynamic situations, tracking agents and actions they produce, events that are results of some action(s), and consequences as new actions, i.e. reactions",
            "http://www.ontologydesignpatterns.org/cp/owl/reaction.owl"
        ],
        "RTMSMapping" : [
            {"RTMS_Code","hasRTMS_Code"},
            "To represent mappings between FSDAS application ontology network, and RTMS ontologies",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/rtmsmapping.owl"
        ],
        "Pollution" : [
            {"carriesPollutant","Carrier","Contributor","EndingPoint","NaturalResourcePollution"," NonNaturalResourcePollution","Observation","Pollutant","Pollution","PrescribedStandardForPollutant","StartingPoint","TimeEntity","Trajectory","TrajectoryPoit","TrajectorySegment","hasPrescribedStandard","startsFrom","hasObservation"},
            "The Pollution ontology design pattern (ODP) intends to model the pollution, the pollutants and their observations at various spatio-temporal points. It also captures the information about the various direct and indirect sources of pollution.",
            ""
        ],
        "Policy" : [
            {"assignedTo","hasAutomationStatus","hasImplementationStatus","hasLanguage","hasPolicyType","hasRequirementLevel","hasStatment","hasSubPolicy","hasValidationProcess","hasVersion","implementedBy","targetsEntity","targetsUsers","AutomationStatus","Descriptor","ImplementationStatus","Language","Policy","PolicyType","Process","RequirementLevel","Statement","Version"},
            "The pattern intends to model policies, their characteristics and their associated entities, such as processes and agents",
            "http://mklab.iti.gr/pericles/Policy_ODP.owl"
        ],
        "PlanConditions" : [
            {"followsPrecondition","hasPoscondition","hasPrecondition","isPostconditionOf","isPostconditionPrecededBy","isPreconditionFollowedBy","isPreconditionOf","precedesPostcondition"},
            "Used for condition planning.",
            "http://www.ontologydesignpatterns.org/cp/owl/planconditions.owl"
        ],
        "Place" : [
            {"hasLocation","isLocationOf","Plce"},
            "To talk about places of things.",
            "http://www.ontologydesignpatterns.org/cp/owl/place.owl"
        ],
        "PharmaInova" : [
            {"Header","Body","Summary","Invoice","has_summary","has_header","has_body"},
            "To describe invoices with the PharmaInnova Model. This schema can be applied to other invoice models.",
            "http://www.isoco.com/ontologies/neon/PharmaInnovaODP.owl"
        ],
        "PeriodicInterval" : [
            {"hasIntervalDurationPerPeriod","hasPeriod","PeriodicInterval"},
            "The goal of this pattern is to represent non-convex intervals where the duration of each internal interval and the duration of the gaps between intervals are constant. These intervals are called periodic intervals within the context of this pattern.",
            "http://delicias.dia.fi.upm.es/ontologies/PeriodicInterval.owl"
        ],
        "Participation" : [
            {"Participation","Participant","hasParticipant","isPartcipantIn","Event","Object"},
            "To represent participation of an object in an event. ",
            "http://ontologydesignpatterns.org/cp/owl/participation.owl"
        ],
        "ParticipantRole" : [
            {"Role","ParticipantRole","participatingInEvent","objectParticipating","roleOfParticipnt","objectIncludedIn","roleIncludedIn","eventIncludedIn"},
            "To represent participants in events holding specific roles in that particular event.",
            "http://www.ontology.se/odp/content/owl/ParticipantRole.owl"
        ],
        "Partof" : [
            {"Entity","hasPart","isPartOf"},
            "To represents entities and their parts.",
            "http://www.ontologydesignpatterns.org/cp/owl/partof.owl "
        ],
        "Parameter" : [
            {"hasParameter","isParameterFor","hasParameterDataValue","Cncept","Parameter"},
            "To represent parameters to be used for a certain concept.",
            "http://ontologydesignpatterns.org/cp/owl/parameter.owl"
        ],
        "Observation" : [
            {"hasObservation","hasParameter","isObservationOf","isParameterOf","inDate","Observation","Parameter"},
            "The intent of this pattern is to represent observations of things, under a set of parameters. Common parameters may be the time and place of the observation, but may be any feature that is observed concerning the specific thing being observed.",
            "http://www.ontologydesignpatterns.org/cp/owl/observation.owl"
        ],
        "ObjectRole" : [
            {"Role","Object"," isRoleOf","hasRole"},
            "To represents objects and the roles they play.",
            "http://ontologydesignpatterns.org/cp/owl/objectrole.owl"
        ],
        "Object_with_States" : [
            {"hasState","isStateOf","Object","State","StateSet"},
            "An object can have different states for which different restrictions apply. The goal of the pattern is to allow modelling the different states of an object and the restrictions on such object for its different states.",
            "http://delicias.dia.fi.upm.es/ontologies/ObjectWithStates.owl"
        ],
        "OOPMetrics" : [
            {"hasClass","hasMethod","hasMetric","hasMetricCategory","hasPackage","hasFloatValue","hasIntegerValue","hasLongName","hasName","hasTag","OOPClass","OOPMethod","OOPMetric","OOPMetricCategory","OOPPackage","OOPProject"},
            "To represent software metrics especially for the purpose of detecting design-flaws in software systems based on these metrics. This is useful for re-engineering the software system., De a reprezenta metricile soft in special in scopul detectarii defectelor de proiectare din sistemele soft pe baza acestor metrici. Acest lucru este folositor pentru reingineria sistemului soft.",
            "http://www.cs.ubbcluj.ro/~ivpop/ontologies/oopmetrics.owl"
        ],
        "NotePattern" : [
            {"Music","Son","SymbolicNote","Accidental","Position","NotePitch","NoteDuration","NoteDynamic","hasMeasure","hasMeasurePosition","hasMidiPitch","isDefinedByOctave","hasLiteralDynamic","hasMidiVelocity","hasNoteDynamic","isDynamicOf","hasNoteDuration","isDurationOfNote","hasNotePitch","isPitchOf","hasAccidental","isAccidentalOf","hasPosition","isPositionOf"},
            "Music Notes",
            "http://ontologydesignpatterns.org/cp/owl/notepattern.owl"
        ],
        "NewsReportingEvent" : [
            {"News","hasPresntationContext","presentedAt","Media","NewsEventReporter","NewsPresentationContext","NewsProvider","NewsReportingEvent","PresentationContext","Reporter","Reporting"},
            "News Reporting",
            "http://semantic.cs.put.poznan.pl/ontologies/newsreportingevent.owl"
        ],
        "NaryParticipation" : [
            {"NaryParticipation","participationIncludes","isIncludedInParticpation"},
            "To represent events with their participants, time, space, etc.",
            "http://www.ontologydesignpatterns.org/cp/owl/naryparticipation.owl"
        ],
        "Musicalobject" : [
            {"Music","Song","Frequency","FundamentalFrequency","PartialFrequency","MusicalObject","MsicalObjectDuration","SoundIntensity","hasDuration","hasFrequency","hasSoundIntensity","isDurationOf","isFrequencyOf","isSoundIntensityOf","hasAttack","hasDecay","hasDurationInSeconds","hasFrequencyMagnitude","hasIntensityValue","hasRelease","hasSustain"},
            "This content ODP models the acoustic features of a music note played in a performance.",
            "https://purl.org/andreapoltronieri/musicalobject"
        ],
        "Move" : [
            {"consistsf","formsPartOf","moved","movedBy","movedFrom","movedTo","tookPlaceAt","wasDestinationOf","wasOriginOf","witnessed","Move","PhysicalObject","Place"},
            "Movement",
            "http://www.ontologydesignpatterns.org/cp/owl/move.owl"
        ],
        "MicroBlogEntry" : [
            {"Social Media","Twitter","Facebook","Instagram","LinkedIn","MicroBlog","MicroBlogSites","Agent","Entity","Media","Location","Topic","Payload","TrutMetric","writtenby","hastimestamp","writtenat","referencestopic","haspayload","presentedon","hasTrustMetric"},
            "Provide a core pattern for capturing information related to microblog entries or social media (e.g. twitter, instagram, facebook, linkedIn, etc.)",
            "https://github.com/cogan-shimizu-wsu/MicroblogEntryOWL/blob/master/MicroblogEntry.owl"
        ],
        "MaterialProperty" : [
            {"Material","MaterialProperty","MaterialPropertywithAssertion","Condition","MaterialPropertyCollection","MaterialPropertyDescriptor","Quantity"},
            "Material Property. To capture the provenance an assertion about a material's properties as well as capture the particulars of the property itself.",
            "https://raw.githubusercontent.com/cogan-shimizu-wsu/MaterialsPropertyOwl/master/matl-prop.owl"
        ],
        "MaterialTransformation" : [
            {"hasCatalyst","hasEmbodiedEnergy","hasEnergyUnit","hasEnergyValue","hasInput","hasOutput","needsEnergy","occursAtTimeInterval","occursInNeighborhood""asLiteral","asNumeric","Catalyst","Energy","EnergyUnit","EnergyValue","MaterialTransformation","MaterialType","Neighborhood","Product","Resource","Material"},
            "Material transformation. To contextualize the transformation process from raw components and the required equipment to a final manufactured artifact",
            "https://raw.githubusercontent.com/Vocamp/MaterialTransformation/master/owl/MaterialTransformationPattern.owl"
        ],
        "MapLegendOntology" : [
            {"Map","Geography","highways","orests","streets","trails","Location","Mountains"},
            "Map of geographical location.",
            "http://stko-exp.geog.ucsb.edu/mlo/map_legend_ontology.owl"
        ],
        "Literal Reification pattern" : [
            {"literal","has lteral","has same literal value as","is literal of","has literal value","comment","contributor","covers requirements","creator","date","description","has component","has intent","has unit test","is specialization of","label","node id","related cps","scenarios","title"},
            "Literal for RDF",
            "https://sparontologies.github.io/literal/current/literal.html"
        ],
        "List" : [
            {"ListItem","Item","OrderedCollection""List","lastItemOf","hasLastItem","firstItemOf","nextItem","previousItem","hasFirstItem"},
            "Representation of ordered collection",
            "http://www.ontologydesignpatterns.org/cp/owl/list.owl"
        ],
        "LinnaeanTaxonomy" : [
            {"Taxonomy","AnimalTaxonomy","PlantTaxonomy","hasDirectHigherRank","hasDirectLowerRank","hasHigherRank","hasLowerRank","Genus","Kingdom","Order","Phylum","Species","Taxon"},
            "Taxonomy",
            "http://www.ontologydesignpatterns.org/cp/owl/linnaeantaxonomy.owl"
        ],
        "LCA Pattern" : [
            {"hasCompartmen","hasLocation","hasProperty","hasTemporalExtent","isInputOf","isOutputOf","performs","playsRoleOf","Activity","Agent","Compartment","ElementaryFlow","Flow","IntermediateFlow","Location","Product","Property","ReferencedProduct","Time","air","soil","water"},
            "Life Cycle Assessment (LCA) studies the environmental impact of products taking into account their entire life-span and production chain. This ontology design pattern specifies key aspects of LCA/LCI data models, namely the notions of flows, activities, agents, and products, as well as their properties",
            "http://descartes-core.org/ontologies/lca/1.0/LCAPattern.owl"
        ],
        "Invoice" : [
            {"Buying","Context","Currency measure","Groundin","Invoice","Line item","Order","Selling","Transaction amount","buyer transaction","grounding"},
            "To represent the core attributes of an invoice",
            "http://www.ontologydesignpatterns.org/cp/owl/invoice.owl"
        ],
        "IntensionExtension" : [
            {"expresses","isAbout","isExpressedBy","isReferenceOf","InformationObject","SocialObject"},
            "To represent the meaning of an information object: the concepts it expresses, the things it is about.",
            "http://ontologydesignpatterns.org/cp/owl/intensionextension.owl"
        ],
        "InformationObjectsAndRepresentationLanguages" : [
            {"conceptualizes","formllyRepresents","hasRepresentationLanguage","isConceptualizedBy","isFormallyRepresentedIn","isRepresentationLanguageOf","FormalExpression","FormalLanguage"," IconicLanguage","IconicObject","Language","LinguisticObject","NaturalLanguage"},
            "Object Representation",
            "http://www.ontologydesignpatterns.org/cp/owl/informationobjectsandrepresentationlanguages.owl"
        ],
        "Information realization" : [
            {"isRealizedBy","realizes","InformationObject","InformationRealizaion"},
            "To represent information objects and their physical realization.",
            "http://www.ontologydesignpatterns.org/cp/owl/informationrealization.owl"
        ],
        "HistoricalMap" : [
            {"PrimeMeridian","MapMathematicalElement","Scale","ReferenceSystem","Projecion","Orientation","MathematicalNote","Collection","HistoricalMap","includes","hasCurrentOwner","Collector","Actor","MapElement","Title","Technique","Subject","SpatialCoverage","Language","Dimension","Note","Material","MapDescriptiveElement","SpatialObject","Creator","created","Cartographer","Publisher","designed","published","isPublishedBy","hasOrientation","hasLanguage","hasProjection","isCreatedBy","hasTitle","hasReferenceSystem","hasSubject","isMadeBy","isPartOf","hasScale","hasNote","hasDimension","hasMathematicalNote","hasPrimeMeridian","isDesignedBy","isMadeOf","isCurrentOwnerOf","hasDateOfPublication","MyProperties","isPublishedAt","isMathematicalNoteOf","isEditedBy","edited","isLanguageOf","isOrientationOf","hasDateOfEdition","isDepictedIn","depicts","hasPlaceOfPublication","hasDateOfCreation","hasColor","type","copy","numberOfSheets","date"},
            "The ontology's intent is to describe a historical map and its attributes.",
            "http://gaia.gge.unb.ca/eg/HistoricalMap.owl"
        ],
        "HazardousSituation" : [
            {"casuallyFollows","exposedTo","Hazard","Object","Cause","Consequence","HazardousEvent","hasDuration","participantIn","hasParticipant","TimeInterval","HazardousSituation","vent","involves"},
            "To model hazardous situations and their associated hazardous events with events' participating objects and the hazards the objects are exposed to with the exposure value.",
            "http://semantic.cs.put.poznan.pl/ontologies/oshdo/HazardousSituation.owl"
        ],
        "Gesture Interaction" : [
            {"Gesture","Human","Movement","BodyPart","Pose","Affordance","Device","uses","Activity","performs","includesgesture","supportsgesture","hasmovement","hasEndPose","hasStartPose"},
            "Ontology pattern to model concepts related to human gesture interactions.",
            "https://w3id.org/hdgi/gesture-interaction-pattern"
        ],
        "GearWaterArea" : [
            {"GearType"," WaterArea","isUsedInWaterArea","isSuitableForGearType","Fishery"},
            "To represent gear types in terms of the water areas where they can be employed to collect aquatic resources",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/gearwaterarea.owl"
        ],
        "CriterionSetter" : [
            {"Criterion","Criterion Setter","criterion set by","has valididty for","sets criterion","is applied in case of","is criterion of use for","is determined by"},
            "The purpose of this pattern is to provide a broader context for criteria modeling. Possible specializations could introduce new kinds of criteria setters representing criteria in detailed contexts (for example: a pattern for describing the success/failure condition for some actions). Possible criteria setters may include requirements, recommendations, constraints etc.",
            "http://criteria-modeling.googlecode.com/svn/trunk/criterion_setter.owl "
        ],
        "GearVessel" : [
            {"Fishery","VesselType","GearType","usesGearType","usedByVesselType"},
            "To represent types of fishing gear with regard to the types of vessel they can be mounted on",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/gearvessel.owl"
        ],
        "GearSpecies" : [
            {"Fishery","AquaticSpecies","GearType","incidentallyCatchesSpecies","targetsSpecies","isCaughtByGearType","isCaughtBy","catchesSpecis"},
            "To represent types of fishing gear with respect to the aquatic species they either are targeted to catch or can accidentally catch",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/gearspecies.owl"
        ],
        "Go Top" : [
            {"Gene","Cellular component","Molecular function","Biological rocess","partOf","Gene Ontology"},
            "To represent types of gene-related entities and their parts.",
            "http://www.ontologydesignpatterns.org/cp/owl/gotop.owl"
        ],
        "Experience & Observation" : [
            {"Engagement","Observation","inActivity","isReflectionOn","isReflectedUponIn","isEngagedIn","hasEngagement","producedObservation","includes"},
            "To represent the epistemological \"missing link\" between a cognitive activity, e.g. the interaction with a cultural object, and any evidence of the effects this activity has on the individuals that are engaged with it; what can collectively be considered as an experience.",
            "https://raw.githubusercontent.com/modellingDH/odp_experience/master/owl/cp_experience.owl.rdfxml"
        ],
        "ExplanationODP" : [
            {"Explanantion","Situation","Agent","Theory","Event","hasCondition","isBasedOn","haExplanans","hasExplanandum","hasSituation"},
            "Describing the process and components of an explanation in different disciplines.",
            "https://github.com/kmitd/various"
        ],
        "WinstonPartWhole" : [
            {"po-component","po-featre","po-member","po-place","po-portion","po-stuff"},
            "Part whole membership.",
            "https://raw.githubusercontent.com/cogan-shimizu-wsu/WinstonPartWhole/master/WinstonPartWhole.owl"
        ],
        "Tagging" : [
            {"Tagging","byAgent","isTagUsedIn","isTaggingAgentIn","usingTag"},
            "To represent a tagging situation, in which someone uses a term, from a list of a folksonomy, to tag something (or the content of something). We might also want to represent the time and the polarity of the tagging.",
            "http://ontologydesignpatterns.org/cp/owl/tagging.owl "
        ],
        "Types of entities" : [
            {"Abstract","Event","Object","Quality"},
            "To identify and categorize the most general types of things in the domain of discourse.",
            "http://www.ontologydesignpatterns.org/cp/owl/typesofentities.owl"
        ],
        "VerticalDistribution" : [
            {"hasResource","hasVerticalDistribution","isResourceOf","isVerticalDistributionOf","hasReferenceYea","AquaticResource","AquaticResourceObservation","VerticalDistribution"},
            "The intent of the pattern is to be able to represent vertical distribution for aquatic resources.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/verticaldistribution.owl"
        ],
        "VesselWaterArea" : [
            {"VesselType","WaterArea","canCrossWaterArea","canBeCrossedByVesselType"},
            "To represent a direct relation between vessel types and water areas regardless of what type of fishing gear is fitted",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/vesselwaterarea.owl"
        ],
        "TimeIndexedSituation" : [
            {"atTime","forEntity","hasTimeIndexedSeting","isTimeIndexFor","TimeIndexedSituation"},
            "To represent time indexed situations.",
            "http://ontologydesignpatterns.org/cp/owl/timeindexedsituation.owl "
        ],
        "TimeIndexedPartOf" : [
            {"Object","Time Indexed Part Of","at time","is tie of","includes whole object","is whole object of","includes part object","is part object of"},
            "To represent objects that have temporary parts.",
            "http://www.ontologydesignpatterns.org/cp/owl/timeindexedpartof.owl "
        ],
        "Time indexed participation" : [
            {"Time indexed participation","includesEvent","includesObject","isEventIncludedIn","isObjectIncldedIn"},
            "To represent participants in events at some time,To represent participants in parts of events.",
            "http://ontologydesignpatterns.org/cp/owl/timeindexedparticipation.owl "
        ],
        "Standard Enforcer Pattern" : [
            {"enforcesGuideline","enforcesStandard","guidelinePrescribedIn","hasDomainScope","hasProcessScope","isEnforcedBy","prescribesGuideline","DomainScope","Guideline","Process","ProcessEnforcingStandard","ProcessScope","Standard"},
            "The remit of the SEP content pattern is to represent the relation between standards and the processes, operations, activities and services that enforce them, the domains they cater to and the scope of that specific process, operation, activity, service within the context of the domain.",
            "http://windermere.aston.ac.uk/~monika/ontologies/Standards-Enforcer-Pattern.owl"
        ],
        "SpeciesNames" : [
            {"AquaticSpecies","hasLocalName","canBeConfusedWith","hasSynonym"},
            "To express the terminological variants and the conceptual similarity that can be sources of confusion between species.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/speciesnames.owl"
        ],
        "SpeciesHabitat" : [
            {"Habitat","hasHabitat","isHabitatFor"},
            "To represent species together with their typical environment in terms of habitat and water area",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/specieshabitat.owl"
        ],
        "SpeciesEat" : [
            {"AquaticSpecies","feedsUpon","isPreyedUponBy","isFoodOf","preyesUpon"},
            "The pattern intends to model the situation that a certain species feed upon other species and that some species are preyed upon by a certain species.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/specieseat.owl"
        ],
        "SpeciesBathymetry" : [
            {"BathymetricRange","hasBathymetricRange","isBathymetricRangeOf","hasRangeMin","hasRangeMax"},
            "To represent species together with their typical environment in terms of bathymetric range and water area",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/speciesbathymetry.owl"
        ],
        "SpeciesConditions" : [
            {"Habitat","SpeciesConditions","AquaticSpecies","BathymetricRange","WaterArea","hasHabitat","inWaterArea","hasBathymetricRange","forSpecies","hasConditons","isWaterAreaFor","isHabitatFor","isBathymetricRangeFor"},
            "This pattern aims at representing the habitat and bathymetric features that are typical for an aquatic species, in the context of a given water area.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/speciesconditions.owl"
        ],
        "SpatioTemporalExtent" : [
            {"hasSpatioTemporalExtent","hasTrajectory","SpatioTemporalExtent","Trajectory"},
            "This pattern models a spatiotemporal extent, i.e., a combination of spatial and temporal extent as a set of generalized trajectories which cannot have temporal overlap. This pattern reuses semantic trajectory pattern as component.",
            "http://krisnadhi.github.io/onto/spatiotemporalextent.owl"
        ],
        "Spatial Graph Adapter (SGA)" : [
            {"SpatialObject","GeoSpatialObject","SpatialRepresentationObject","represents","Attribute","Value","Type","ContexualizedRelation","hasContextRelation"},
            "To answer the modern, interdisciplinary questions asked within the Building domain, industry tools and data standards need to become far more interoperable in order to be able to provide a full and accurate set of analysis to engineers and designers. To provide this full picture from which to make decisions, we needed a way to resolve the spatial data that tools provide in order to synthesize it together. In addition to missing, incorrect, and inconsistent information, there is also the challenge of not being able to use existing spatial patterns to capture the full granularity or specificity of the geospatial descriptions required to capture full and dynamic geometric contexts.",
            "https://raw.githubusercontent.com/HollyFerguson/Spatial-Graph-Adapter-Pattern/master/SGA_Protege_OWL.owl "
        ],
        "Social Reality" : [
            {"SocialReality","context","has_OR","is_OR","counts-as","BF","C","OR"},
            "Capture Searle's theory on observer relative and institutional facts, used in creating social reality. See also the OWL 2 Agent-Role pattern.",
            "http://purl.org/net/social-reality"
        ],
        "SmartHome TimeInterval" : [
            {"SmartHomeTimeInterval","SmartHomeTemporalDistance","hasUpperTimestampValue","hasLowerTimestampValue"},
            "This pattern allows us to represent a temporal distance between two timestamps within an observation process in a SmartHome. There are other situations where we need to measure the interval (temporal distance) in the form of time steps regardless of the exact dates indicating the boundaries of the interval.",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/time.owl "
        ],
        "SmartHome Situation" : [
            {"SmartObjectSituation","State"},
            "Smart Home Situation",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Situation.owl "
        ],
        "SmartHome Sensing" : [
            {"SensingProcess"," martHomeSensor","SmartHomeSensorOutput"},
            "Smart Home Sensing",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Sensing.owl"
        ],
        "SmartHome Property" : [
            {"SmartHomeProperty"},
            "Smart Home Property",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Property.owl"
        ],
        "SmartHome Place" : [
            {"SmartHome","SmartHomeSection"},
            "To represent a SmartHome as a place (specialization of http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#PhysicalPlace) which contains a number of sections (other physical places) and is also seen as a platform (e.g. a platform for a sensor network).",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Place.owl"
        ],
        "SmartHome Object" : [
            {"Location","Mobilebject","NodeHolder","NonMobileObject","SmartHomeAgent","SmartHomeObject","SmartObject"},
            "Smart Home Object",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Object.owl"
        ],
        "SmartHome Network" : [
            {"receivesDataFrom","sendsDataTo","DataReceiverNode","DataSenderNode","Network","Node","NodeStation","ReceiverNodeStation","SenderNodeStation","SmartHomeDeployment"},
            "This pattern relies on both the SSN ontology and DUL in order to represent sensors and other techniqually needed objects to deploy a network in a smart home environment.",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Network.owl "
        ],
        "SmartHome Geometry" : [
            {"eastOf","hasDirectionalRelation","hasSpatialRelatin","northEastOf","northOf","northWestOf","southEastOf","southOf","southWestOf","westOf","SmartHomeGeoFeature"},
            "To represent geospatial relations between objects.",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_Geometry.owl "
        ],
        "SmartHome FeatureOfInterest" : [
            {"SmartHomeFeatureOfInterest"},
            "To represent the specific feature (property) of a certain object that is observed (measured) by a sensing process. Since an object can have many features, it is not enough to point at the object itself, but one also need to specify the property that is in focus.",
            "http://ecareathome-ontology.mpi.aass.oru.se/patterns/SmartHome_FeatureOfInterest.owl"
        ],
        "SmartHome Event" : [
            {"ComplexEvent","EventCondition","Manifestation"},
            "This pattern is used to represent events in the context of smart environments. An event in this pattern is represented in the form of either a Manifestation or a Complex Event, where a manifestation represents the occurrence of a specific situation of an object which can be directly captured from sensor data (\"the TV is switched on\"), whereas a complex event is defined based on its preconditions that can involve different events (e.g., \"watching TV\" happens when \"the TV is switched on\" and \"someone is sitting on the couch\").",
            "https://w3id.org/smartenvironment/event.owl"
        ],
        "SimpleTopic" : [
            {"farTopicFrom","hasCoreConcept","Topic","hasSubTopic","isSubTopicOf","SubTopic","nearTopicTo","overlappingTopic"},
            "It is a simplified version of the ontology \"ontopic\". It is used when we want to talk about the topics of a documents and their relationships.",
            "http://www.ontologydesignpatterns.org/cp/owl/topic.owl"
        ],
        "Situation" : [
            {"hasSetting","isSettingFor","Situation"},
            "To represent contexts or situations, and the things that are contextualized.",
            "http://www.ontologydesignpatterns.org/cp/owl/situation.owl"
        ],
        "SimpleOrAggregated " : [
            {"hasAggregatedMember","isAggregatedMemberOf","AggregatedObject","Object","ObjectByCardinality","SimpleObject"},
            "The goal of this pattern is to represent objects that can be simple or aggregated (that is, several objects gathered in another object acting as a whole)",
            "http://delicias.dia.fi.upm.es/ontologies/SimpleOrAggregated.owl "
        ],
        "Sequence" : [
            {"directlyFollows","directlyPrecedes","follows","precedes"},
            "To represent sequence schemas. It defines the notion of transitive and intransitive precedence and their inverses.",
            "http://ontologydesignpatterns.org/cp/owl/sequence.owl "
        ],
        "NewsReportingEvent" : [
            {"NewsProvider","News","Agent","ReportingEvent","Media","NewsEventReporter","NewsReportingEvent","ActualEvent","NewsPresentationContext","isBasedOn","owns","actsFor"},
            "The pattern can be used for modelling situations in which we are not certain that a particular actual event has the properties which were described in a news message. We want to define the properties of an actual event which were reported (time, place, actors, subevents, cause, effect etc.), but not to treat them as universal, verified knowledge. ",
            "http://semantic.cs.put.poznan.pl/ontologies/newsreportingevent.owl "
        ],
        "RelativeRelationship" : [
            {"Entity","Property","Usage","RelativeExistence","relativeExistenceOf","hasProperty","usageType","Domain","hasDomain","RelationshipDescription","hasAttribute","Attribute","hasScope","Scope","LevelofDetail","hasBound"},
            "For dynamically conceptualizing, establishing, tracking, and updating relative relationships and dependencies between entities (real or representational) of a physical, temporal, and/or importance scope.",
            "https://curate.nd.edu/downloads/9p29086355b"
        ],
        "Region" : [
            {"hasRegion","isRegionFor","hasRegionDataValue","Region"},
            "To represent and reason on values of attributes of things, by explicitly talking about the dimensions (\"regions\") of the attributes, which include those values.",
            "http://ontologydesignpatterns.org/cp/owl/region.owl"
        ],
        "RecurrentSituationSeries" : [
            {"hasEstimatedTimePeriod","hasImmediateNextSituation","hasImmediatePreviousSituation","hasMeasuredTimePeriod","hasMemberSituation","hasNextSituation","hasPreviousSituaion","hasTimePeriod","hasTimePeriodBeforeNextSituation","hasUnifyingFactor","hasUnifyingSituation","involvesUnifyingFactor","isEstimatedTimePeriodOf","isInvolvedInUnifyingSituation","isLocallyInconsistentWith","isMeasuredTimePeriodOf","isSituationMemberOf","isTimePeriodBeforeNextSituationOf","isTimePeriodOf","isUnifyingFactorOf","isUnifyingSituationOf","isValidIn","isTheLastSituation","situationNumber","RecurrentSituationSeries","Situation","TimePeriod","UnifyingFactor","UnifyingSituation"},
            "To represent recurrent situation series as situations and collections of consecutive situations, with a regular time period between situations and unifying factors.",
            "http://www.ontologydesignpatterns.org/cp/owl/recurrentsituationseries.owl"
        ],
        "ResourceAbundanceObservation" : [
            {"AbundanceLevel","ResourceAbundanceObservation","hasReferenceYear","hasAbundanceLevel","hasResource","isResourceOf","isAbundanceLevelOf"},
            "The intent of the pattern is to be able to represent observations of aquatic resources, where the observations have been made a certain year and has certain other parameters.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/resourceabundanceobservation.owl "
        ],
        "ResourceExploitationObservation" : [
            {"ResourceExploitationObservation","hasReferenceYear","hasResource","hasExploitationRate"," ExploitationRate","ExploitationState","hasExploitationState","isExploitationStateOf","isResourceOf","isExploitationRateOf"},
            "The intent of the pattern is to be able to represent observations of aquatic resources, where the observations have been made a certain year and has certain other parameters.",
            "http://www.ontologydesignpatterns.org/cp/owl/fsdas/resourceexploitationobservation.owl "
        ],
        "RoleTask" : [
            {"role","has task","Task","is task ok"},
            "To represent the assignment of tasks to roles",
            "http://www.ontologydesignpatterns.org/cp/owl/taskrole.owl"
        ],
        "ScorePart" : [
            {"Part","Section"," Instrument","Voice","HomogeneousFragment","hasMidiProgram","hasStaff","hasClef","hasTempo","hsMetric","isPlayedBy","hasVoice","hasSection","hasFragment","isFragmentOf"," isSectionOf","isVoiceOf","playsPart"},
            "This content ODP formalises the structure and the hierarchies of a music score/symbolic representation system.",
            "http://ontologydesignpatterns.org/cp/owl/scorepart.owl"
        ],
        "Actuation-Actuator-Effect" : [
            {"Actuation","involves","trigger","implements","satisfies","Procedure","Actuator","Effect","impacts","ImpactedProperty","FeatureofInterest"},
            "This ODP intents to model the relationship between an Actuator and the Effect it has on its environment through Actuations. It structures an Actuator ontology :",
            "http://www.irit.fr/recherches/MELODI/ontologies/AAE.owl "
        ],
        "Affordance" : [
            {"hasParameter","hasTask","holds","isHeldBy","affordanceStrength","Afforance","Frame","Situation","TaskParameter"},
            "To represent the model for supporting the action selection mechanism.",
            "http://www.ontologydesignpatterns.org/ont/mario/affordance.owl "
        ],
        "Activity" : [
            {"hasDependent","hasOutcome","hasPart","hasParticipant","hasRequirement","isDependentOf","isPartOf","isPrecededBy","isRequirementOf","precedes","produces","supports"," takesPlaceAt","hasDuration","hasEnd","hasStart","Activity","Fixedctivity","FlexibleActivity","Outcome","Place","Requirement"},
            "To incorporate the general two perspectives of activities: a workflow perspective, which are often observed in planning-related applications, and a spatiotemporal perspective, which are often found in geographic activity analysis.",
            "http://descartes-core.org/ontologies/activities/1.0/ActivityPattern.owl  "
        ],
        "Born Digital Archives" : [
            {"hasCreator","hasPart","Creator","File","Fonds","Item","Series","Unt"},
            "The pattern intends to model the domain of born digital archives.",
            "http://mklab.iti.gr/pericles/BornDigitalArchives_ODP.owl"
        ],
        "City Resident Pattern" : [
            {"Address","Building","Citizenship","City","ControlledEntity","Country","HomeType","LandArea","Organization","Person","Residence","Resident","ResidentThing","ResidentilRelationship","ResidentObjectProperty","citizenOf","entity","forCity","forCountry","hasAddress","hasHomeType","hasResidence","hasResidentialRelationship","operates","owns","apartment","condominium","freeload","hotel","house","lease","openLand"},
            "This file defines an ontology design pattern for City \"Resident.” Why is the development a Resident pattern important for the development of a city data on-tology?",
            "http://ontology.eil.utoronto.ca/cdm/Resident.owl "
        ],
        "Co-participation" : [
            {"coparticipatesWith"},
            "To represent two objects that both participate in a same event.",
            "http://www.ontologydesignpatterns.org/cp/owl/coparticipation.owl "
        ],
        "CollectionEntity" : [
            {"Collection","Entity","hasMember","isMemberOf"},
            "To represent collections, and their entities, i.e. to represent membership.",
            "http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl"
        ],
        "CommunicationEvent" : [
            {"ContactMechanism","isValidContactMechanismFor","CommunicationEventRole","mediumOf","CommunicationEvent","EventDuration","eventStartTime","RelationshipDuration","relationshipStartTime","PartyRole","RelationshipPartyRole","roleInRelationship","PartyRelationship","includesCommunication","relationshipIncludes","relationshipHasDuration","EmailCommunication","throughMedium","e-mail","PhoneCommunication","Phone","CommunicationPurpose","purposeOfEvent","WebSiteCommunication","Website","FaceToFaceCommunication","roleOfParty","partyParticipating","inRelationship","Party","partyInvolvedIn","CommunicationEventPartyRole","partyInRelationship","hasValidContactMechanism","eventRoleIncludedIn","LetterCorrespondence","Letter","FaxCommunication","Fax","roleOfEvent","partyInEvent","inCommunicationEvent","eventIncludes","communicationHasSetting","eventHasPurpose","eventHasDuration","hasEventStatus","CommunicationEventStatus","statusOfEvent","isDurationOfEvent","isDurationOfRelationship","relationshipEndTime","eventEndTime"},
            "To model communication events, such as phone calls, e-mails and meetings, their involved parties and the roles and relations of the parties in the context of the communication events.",
            "http://www.ontology.se/odp/content/owl/CommunicationEvent.owl"
        ],
        "Complaint Ontology Pattern" : [
            {"basedOn","expressedIn","hasComplaintMotivation","justifiedBy","madeBy","supprtedBy","hasSpace","hasStampTime","hasTimeOccurrence","Agent","Complainant","Complaint","Complaint_Recipient","Complaint_Recipient","Fact","Medium","Motivation","Request","ThirdParty","partOf","addressedTo"},
            "To represent core constituents found commonly in complaints across domains.",
            "http://ontoology.linkeddata.es/publish/cop/index-en.html "
        ],
        "Componency" : [
            {"Object","hasComponent","isComponentOf"},
            "To represent (non-transitively) that objects either are proper parts of other objects, or have proper parts",
            "http://www.ontologydesignpatterns.org/cp/owl/componency.owl"
        ],
        "ComputationalEnvironment" : [
            {"IO_Device","GPU","Processor","CPU","NetworkInterface","Disk","Memory","Hardware","Software","PUType","CPUArchitecture","Kernel","OperatingSystem","OS_Shell_Environment","hasKernelVersion","hasFrequency","hasCores","hasVirtualAddress","hasPhysicalAddress","EnvironmentVariable"},
            "The pattern is intended to support comparison and reproducibility of computational analyses.",
            "https://raw.githubusercontent.com/mcheatham/computationalEnvironmentODP/master/docs/ComputationalEnvironment.owl"
        ],
        "ConceptGroup" : [
            {"Concept","ConceptGroup","MembershipRestriction","BroaderNarrowerRelation"},
            "This CP allows designers to represent concept group defined by intention (all concepts satisfying group membership condition) or by extension (all concepts referring a group).",
            "http://sites.google.com/site/pierreyvesvandenbussche/resources/ConceptGroup.owl"
        ],
        "ConceptTerms" : [
            {"Concept","ConceptTermsRelation","PreferredTerm","SimpleNonPreferredTerm","Term","CompoundPreferedTerm","hasForConcept"},
            "This CP allows designers to represent jointly conceptual and linguistic part of a vocabulary.",
            "http://sites.google.com/site/pierreyvesvandenbussche/resources/ConceptTerms.owl"
        ],
        "Constituency" : [
            {"Entity","hasConstituent","isConstituentOf"},
            "To represent the constituents of a layered structure.",
            "http://www.ontologydesignpatterns.org/cp/owl/constituency.owl"
        ],
        "Controlflow" : [
            {"AbstractMergingTask","ActionTask","ActivationTask","BooleanCaseTask","BranchingTsk","CaseTask","ConcurrencyTask","ControlTask","DecisionActivity","DeliberationState","DeliberationTask","EndingTask","LoopTask","MergingTask","SynchroTask"},
            "To represent control flows: activation, branching, decisions, concurrency, etc.",
            "http://www.ontologydesignpatterns.org/cp/owl/controlflow.owl "
        ],
        "DataTransformationPattern" : [
            {"executedIn","hasDataType","hsPayload","implements","occursIn","performsInputRole","performsOutputRole","performsParameterRole","providesInputDataRole","providesOutputDataRole","providesParameterRole","Algorithm","ComputationalEnvironment","DataTransformation","DataType","EntityWithProvenance","InputDataRole","OutputDataRole","ParameterRole","Payload","SpatiotemporalExtent","aData"},
            "Data Transformation Pattern",
            "https://raw.githubusercontent.com/cogan-shimizu-wsu/DataTransformationPattern/master/DataTransformationPattern.owl"
        ],
        "Description" : [
            {"Description","Concept","is defined in","is concept used in","defines","uses concept"},
            "To formally represent a conceptualization or a descriptive context.",
            "http://www.ontologydesignpatterns.org/cp/owl/description.owl"
        ],
        "Description in Range" : [
            {"DescriptionInRange","Entity","isRangedByValue","hasInclusiveLowerBoundValue","hasNonInclusiveLowerBoundValue","hasInclusiveUpperBoundValue""hasNonInclusiveUpperBoundValue","isDescribedBy","describes"},
            "This pattern allows one to range the conceptualization of a descriptive context within specific borders defined by means of literal values.",
            "https://w3id.org/food/ontology/dir"
        ],
        "DescriptionAndSituation" : [
            {"describes","isDescribedBy","isSatisfiedBy","satisfies","Situation","Concept"},
            "Description and Situation",
            "http://www.ontologydesignpatterns.org/cp/owl/descriptionandsituation.owl"
        ],
        "DetectorFinalState" : [
            {"DetectorFinalState","Physics","AND/OR","Logic","BinaryRelation","SelectionCriteia","PhysicalValue","FinalStateObject","PhysicalQuantity","Unit","NumericalValue","Number","BaseDefinition","PhysicsObject","EventLevelQuantity","hasOperand","hasFirstArgument","hasSecondArgument","refersToObject"},
            "This pattern represent schematic model for high-energy physics experiment data.",
            "https://www.dropbox.com/s/uy0bh33wsdzx6bp/dectectorfinalstate.owl?dl=0"
        ],
        "DigitalVideo" : [
            {"Audio","Video","DigitalVideo","Codec","AudioCodec","VideoCodec","Stream","AudioStream","VideoStream","SubtitleStream","Containe","Descriptor","AnalogBroadcastStandard","AspectRatio","Bit Rate","ChromaFormat","CodingStandard","ColourSpaceType","CompressionType","EmbeddingType","FrameRate","FrameSize","PlaybackDuration","RangeType","SampleRate","ScanType","SetOfStandards","E.g. SubRip, SubViewer, etc.","VideoCodecLevel","VideoCodecProfile","VideoQualityMeasurement","VideoQualityMetric","YUVSampleRange","hasBitRate","wrappedBy","hasStream","hasAudioStream","hasVideoStream","hasSubtitleStream","hasCodingStandard","hasRangeType","hasVideoQualityMeasurement","hasChromaFormat","hasEmbeddingType","hasAspectRatio","hasSubtitleTextFormat","hasVideoQualityMetric","hasCompressionType","hasScanType","hasVideoCodecProfile","hasColourSpaceType","hasFrameSize","hasSetOfStandards","processedBy","hasAnalogBroadcastStandard","hasVideoCodecLevel","hasFrameRate","hasPlaybackDuration","hasYUVSampleRange","hasSampleRate"},
            "The pattern intends to model digital video files, their components and other associated entities, such as codecs and containers",
            "http://mklab.iti.gr/pericles/DigitalVideo_ODP.owl"
        ],
        "Disposition" : [
            {"Bearer","Trigger","Disposition","Realization","hasDisposition","inheresIn","hasTriggerR","has_triggerD","hasRealization","Bioogy"},
            "This pattern allow the representation of non-probabilistic dispositions with unique triggering and realization process types.",
            "Roehl-jansen_disposition-pattern.owl "
        ],
        "EthnicGroup" : [
            {"EthnicGroup","hasIsland","Person","hasTown","hasCountry","hasEthnicGroup","hasContient","hasOfficeHolder","Continent","Place","River","Island","AdministrativeRegion","Language"},
            "To represent the encyclopedic knowledge expressed by an object typed as EthnicGroup",
            "http://ontologydesignpatterns.org/ekp/owl/EthnicGroup.owl "
        ],
        "EventCore" : [
            {"DASE_RULE","freshProp1","freshProp2","hasInformationObject","hasSpatioTemporalExtent","providesParticipantRole","subEventOf","subSpatioTemporalExtentOf","Event","InformationObject","ParticipantRole","SpatioTemporalExtent"},
            "The purpose of this pattern is to provide a minimalistic model of event where it is not always possible to separate its spatial and the temporal aspects, thus can model events that move or possess discontinuous temporal extent. Events according to this model has at least one participant, attached via a participant-role, and may have additional descriptive information through its information object.",
            "http://krisnadhi.github.io/onto/event.owl"
        ],
        "EventProcessing" : [
            {"SimpleEventObject","EventObject","CompositeEventObject","ComplexEventObject","hasEventObjectPart","SensorOutput","hasSubEventObject","EventObjectHeader","hasEventObjectTime","hasEventDuration","hasEventObjectAttributeValue","hasEventObjectAttributeDataValue","isEventObjectHeaderOf","EventObjectPart","EventObjectBody","isEventObjectBodyOf","hasEventObjectHeader","informationAboutEvent","hasEventLocation","hasEventObjectBody","refersToEventOjectConstituent","refersToEventObjectComponent","isEventObjectComponentOf","hasEventObjectComponent","isEventObjectPartOf","hasSensorReadingValue","hasDirectSubEventObject","isDirectSubEventObjectOf","isSubEventObjectOf","hasEventObjectSystemTime","hasEventObjectExpirationTime","hasEventObjectSamplingTime","hasEventObjectApplicationTime"},
            "To model event objects (in the context of complex event processing), their attributes, and their relations actual events, and sensor readings producing the events. Different types of event objects, such as complex, composite, and simple events are modelled, preoperties for expressing relations between event objects, such as constituency and componency are expressed, and attributes of event objects, such as timestamps and other data values.",
            "http://www.ontologydesignpatterns.org/cp/owl/eventprocessing.owl"
        ]
}