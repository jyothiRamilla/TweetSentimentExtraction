##streamlit run app.py

# Core Pkgs
import streamlit as st 
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)
SEQUENCE_LENGTH = 300

def main():
	"""Sentiment Extraction App"""

	st.title("Sentiment Extraction From the Tweet")
	st.text("Build with Streamlit ")

	activities = ["Sentiment","About"]
	choice = st.sidebar.selectbox("Select Activty",activities)
	#image_file1 = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
	#if image_file1 is not None:
	#	our_image1 = Image.open(image_file1)

	if choice == 'Sentiment':
		tokenizer = Tokenizer()
		model = tf.keras.models.load_model("tweet.h5")
		def decode_sentiment(score, include_neutral=True):
			if include_neutral:
				label = NEUTRAL
				if score <= SENTIMENT_THRESHOLDS[0]:
					label = NEGATIVE
				elif score >= SENTIMENT_THRESHOLDS[1]:
					label = POSITIVE
				return label
			else:
				return NEGATIVE if score < 0.4 else POSITIVE
		def predict(text, include_neutral=True):

			#start_at = time.time()
			# Tokenize text
			x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
			# Predict
			score = model.predict([x_test])[0]
			# Decode sentiment
			label = decode_sentiment(score, include_neutral=include_neutral)
			st.text(label)
			st.text(score)

		d= st.text_input("Enter text")
		st.text(d)
		result = predict(d)
		
	elif choice == 'About':
		st.subheader("Face filters and features detection App")
		st.markdown("Built with Streamlit by Jyothi")
		st.text("Jyothi Ramilla")
		st.success("jyothi99162@gmail.com")
	

if __name__ == '__main__':
		main()