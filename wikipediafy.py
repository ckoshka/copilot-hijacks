from transformers import pipeline, AutoModelForConditionalGeneration, AutoTokenizer
pipeline = pipeline(model="bart-large-convert-to-wikipedia")
#This model draws on its existing knowledge and a provided source to generate a Wikipedia-style executive summary of a given topic.

pipeline("MUSK: Well, I was born in South Africa, lived there until I was 17. Came to North America of my own accord, against my parent’s wishes. And was in Canada for a few years. I started school there which is where I met my wife. Transferred down to the University of Pennsylvania and got a degree in physics, degree in business at Wharton")
#Should return:
#Elon Musk
#Elon Musk, born in South Africa [1], is an American engineer, entrepreneur, and philanthropist. He is the founder, CEO, and CTO of SpaceX, an American aerospace company. Living in Canada for a few years, where he met his current wife, he transferred down to the University of Pennsylvania and graduated with a degree in physics and a degree in business at Wharton.

pipeline("The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the complex code from the library, offering a simple API dedicated to several tasks, including Named Entity Recognition, Masked Language Modeling, Sentiment Analysis, Feature Extraction and Question Answering. See the task summary for examples of use.")
#Should return:
#Pipelines (Huggingface object)
Pipelines are inferencing objects responsible for abstracting Huggingface's library, providing a unified API for tasks such as Named Entity Recognition, Masked Language Modeling, Sentiment Analysis, Feature Extraction and Question Answering.

pipeline("Certain engineering applications of the latter sort of problem arose in the work of the Engineering Research Section, Fire Control Design Division, at Frankford Arsenal. In these applications, the function /(«; *i, • • • , x„) was sufficiently complicated so that the standard method for dealing with non linear least square problems1 failed to converge. Two techniques for dealing with this situation were developed by the section under the direction of J. G. Tappert. One of these was an original suggestion of my associate K. Levenberg.2")
#Should return:
#Engineering Research Section, Fire Control Design Division, at Frankford Arsenal
#The Engineering Research Section, Fire Control Design Division, at Frankford Arsenal, is a division of the United States Air Force. It is responsible for the design of the air defense systems of the United States Air Force. It pioneered in designing solutions for non-linear least square problems. Two techniques for dealing with this situation were developed by the section under the direction of J. G. Tappert.
