import streamlit as st
import pickle
#load the saved machine learning model
loaded_model = pickle.load(open('attacks_model.pkl', 'rb'))

#function that return the prediction 
def label_predict(a):
	if a[0]==0:
		result='this is a BENIGN attack'
	elif a[0]==1:
		result='this is a DDOS attack'
	elif a[0]==2:
		result='this is a DOS attack'
	else:
		result='this is a Port Scan'
	return result

#the main function that will run
def main():
	st.title("Identify type of CyberSecurity Attack Using Machine Learning")
	
#some style of streamlit
	col1, col2, col3 , col4,col5 = st.columns(5)

	with col1:
		#inputs of the 5 features
		number1 = st.number_input('Bwd Packet Len Std',key=1,step=5,min_value=0,max_value=7000)
	with col2:
		number2 = st.number_input('Total Backwd Packets',key=2,step=0.2)
	with col3:
		number3 = st.number_input(' Flow Duration',key=3,step=5,min_value=0,max_value=100000000)
	with col4:
		number4 = st.number_input(' Flow IAT Min',key=4,step=5,min_value=0,max_value=120000000)
	with col5:
		number5 = st.number_input(' Destination Port',key=5,step=10,min_value=0,max_value=70000)


#the button to run the prediction and show the result
	if st.button("Identify"):
		result= label_predict(loaded_model.predict([[number5,number1,number2,number3,number4]]))
		#st.header(result)
		st.success(result)


	st.header('Identify type of CyberSecurity Attack Using the difference of features (from the DATASET)')
	st.image('img1.png')
	st.image('img2.png')
	st.image('img3.png')
	st.image('img4.png')

if __name__ == '__main__':
    main()