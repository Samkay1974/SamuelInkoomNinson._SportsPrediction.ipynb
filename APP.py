{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b51fdb84-00b2-4585-8414-b8edbb57b372",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "23fd9494-705e-4758-8025-30b0c35cfd71",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-06-23 22:34:40.449 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\LENOVO\\OneDrive - Ashesi University\\Documents\\Python Scripts\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-06-23 22:34:40.451 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "# Load the trained model\n",
    "with open('Ratings_Predictor.pkl', 'rb') as file:\n",
    "    best_m = pickle.load(file)\n",
    "\n",
    "# Define the features to be used for prediction\n",
    "features = [\n",
    "    'movement_reactions', 'mentality_composure', 'passing', 'potential',\n",
    "    'dribbling', 'power_shot_power', 'mentality_vision', 'attacking_short_passing'\n",
    "]\n",
    "\n",
    "# Create a function to make predictions\n",
    "def predict_player_rating(input_data):\n",
    "    df = pd.DataFrame([input_data], columns=features)\n",
    "    prediction = best_m.predict(df)\n",
    "    return prediction[0]\n",
    "\n",
    "# Streamlit app\n",
    "st.title('Player Rating Predictor')\n",
    "\n",
    "# Create input fields for each feature\n",
    "input_data = {}\n",
    "for feature in features:\n",
    "    input_data[feature] = st.number_input(f'Enter {feature}', value=0)\n",
    "\n",
    "# When the 'Predict' button is clicked, make the prediction\n",
    "if st.button('Predict'):\n",
    "    rating = predict_player_rating(input_data)\n",
    "    st.write(f'The predicted player rating is: {rating}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e903c39-d567-463d-8cef-7babd74801e4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
