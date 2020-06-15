from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    # df = pd.read_excel(r'G:\Npontu\Internship_2019\betting\Datasets\EPL\data\merged_epl.xlsx')

	# labelEncoder = LabelEncoder()

	# df['HomeTeam_En'] = labelEncoder.fit_transform(df.iloc[:,0].astype(str))
	# df['AwayTeam_En'] = labelEncoder.fit_transform(df.iloc[:,1].astype(str))

	# X =  df[['HomeTeam_En', 'AwayTeam_En']]
	# X1 = df[['HomeTeam_En', 'AwayTeam_En', 'SportyH', 'SportyD', 'SportyA']]

	# y =  np.array(df['FTR'])
	# y1 = np.array(df['FTHG'])
	# y2 = np.array(df['FTAG'])

	# target = y
	# target1 = y1
	# target2 = y2

	# features = np.array(X)
	# features1 = np.array(X1)

	# train_features, test_features, train_labels, test_labels = train_test_split(features1, target, test_size=0.3, random_state=42)

	# mod = XGBClassifier()
	# model = mod.fit(train_features, train_labels)

    # root = Path(".")
    # my_path = root/"models"/"chat.pkl"

	# # predicted_labels = model.predict(test_features)

	# pkl_filename = "bet_pickle.pkl"
	# with open(pkl_filename, 'wb') as file:
	# 	pickle.dump(model, file)

	# with open(pkl_filename, 'rb') as file:
	# 	clf2 = pickle.load(file)