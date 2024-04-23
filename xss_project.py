# -*- coding: utf-8 -*-
"""XSS Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XReRV2BFovbL2UfZLQykpgwR_296rbEo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report

from google.colab import drive
drive.mount("/content/drive")

dataset = pd.read_csv("/content/drive/My Drive/XSS Dataset/Data_66_featurs.csv")

dataset.shape

dataset.isnull().sum()

dataset.columns

dataset.describe()

# Splitting Data into training and testing
x = dataset.drop(columns="Label",axis=1)
y = dataset["Label"]

# Data Splitting
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 1)

# Model Selection
model = DecisionTreeClassifier()

model.fit(x_train,y_train)

train_prediction = model.predict(x_train)

test_prediction = model.predict(x_test)

Train_Accuracy = accuracy_score(train_prediction,y_train) * 100

print("Accuracy Score for the Train data detection : " + str(round(Train_Accuracy,1)) + "%")

Test_Accuracy = accuracy_score(test_prediction,y_test) * 100

print("Accuracy Score for the Test data detection : " + str(round(Test_Accuracy,1)) + "%")

#Plot the graph for visualization
plt.scatter(Train_Accuracy, Test_Accuracy, marker='o', color='blue', label='Data Points')
plt.plot([0, 100], [0, 100], linestyle='--', color='gray', label='Line of Equality')
plt.title("Relationship between Training and Testing Accuracy")
plt.legend()
plt.grid(True)
plt.show()

# Data Visualization using heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(dataset.corr(), annot=True, cmap='viridis', fmt=".2f")
plt.title("Heatmap of Training and Testing Accuracy")
plt.show()

feature_names = ['url_length', 'url_special_characters', 'url_tag_script', 'url_tag_iframe', 'url_attr_src', 'url_event_onload', 'url_event_onmouseover', 'url_cookie', 'url_number_keywords_param', 'url_number_domain', 'html_tag_script', 'html_tag_iframe', 'html_tag_meta', 'html_tag_object', 'html_tag_embed', 'html_tag_link', 'html_tag_svg', 'html_tag_frame', 'html_tag_form', 'html_tag_div', 'html_tag_style', 'html_tag_img', 'html_tag_input', 'html_tag_textarea', 'html_attr_action', 'html_attr_background', 'html_attr_classid', 'html_attr_codebase', 'html_attr_href', 'html_attr_longdesc', 'html_attr_profile', 'html_attr_src', 'html_attr_usemap', 'html_attr_http-equiv', 'html_event_onblur', 'html_event_onchange', 'html_event_onclick', 'html_event_onerror', 'html_event_onfocus', 'html_event_onkeydown', 'html_event_onkeypress', 'html_event_onkeyup', 'html_event_onload', 'html_event_onmousedown', 'html_event_onmouseout', 'html_event_onmouseover', 'html_event_onmouseup', 'html_event_onsubmit', 'html_number_keywords_evil', 'js_file', 'js_pseudo_protocol', 'js_dom_location', 'js_dom_document', 'js_prop_cookie', 'js_prop_referrer', 'js_method_write', 'js_method_getElementsByTagName', 'js_method_getElementById', 'js_method_alert', 'js_method_eval', 'js_method_fromCharCode', 'js_method_confirm', 'js_min_length', 'js_min_define_function', 'js_min_function_calls', 'js_string_max_length']

print("Decision Tree Rules:")
tree_rules = []
def traverse_tree(node, depth):
    indent = "  " * depth
    if node >= len(model.tree_.feature):
        return
    if model.tree_.children_left[node] == model.tree_.children_right[node]:
        tree_rules.append(f"{indent}Leaf node: Predicted class {model.classes_[np.argmax(model.tree_.value[node])]}")
    else:
        feature = model.tree_.feature[node]
        threshold = model.tree_.threshold[node]
        if feature >= len(feature_names):
            return
        if threshold == -2:
            tree_rules.append(f"{indent}Leaf node: Predicted class {model.classes_[np.argmax(model.tree_.value[node])]}")
        else:
            tree_rules.append(f"{indent}If feature {feature_names[feature]} <= {threshold}:")
            traverse_tree(model.tree_.children_left[node], depth + 1)
            tree_rules.append(f"{indent}else:")
            traverse_tree(model.tree_.children_right[node], depth + 1)

traverse_tree(0, 0)
print("\n".join(tree_rules))

from sklearn.tree import export_graphviz
import graphviz

# Update feature names
feature_names = [
    'url_length', 'url_special_characters', 'url_tag_script', 'url_tag_iframe', 'url_attr_src', 'url_event_onload',
    'url_event_onmouseover', 'url_cookie', 'url_number_keywords_param', 'url_number_domain', 'html_tag_script',
    'html_tag_iframe', 'html_tag_meta', 'html_tag_object', 'html_tag_embed', 'html_tag_link', 'html_tag_svg',
    'html_tag_frame', 'html_tag_form', 'html_tag_div', 'html_tag_style', 'html_tag_img', 'html_tag_input',
    'html_tag_textarea', 'html_attr_action', 'html_attr_background', 'html_attr_classid', 'html_attr_codebase',
    'html_attr_href', 'html_attr_longdesc', 'html_attr_profile', 'html_attr_src', 'html_attr_usemap',
    'html_attr_http-equiv', 'html_event_onblur', 'html_event_onchange', 'html_event_onclick', 'html_event_onerror',
    'html_event_onfocus', 'html_event_onkeydown', 'html_event_onkeypress', 'html_event_onkeyup', 'html_event_onload',
    'html_event_onmousedown', 'html_event_onmouseout', 'html_event_onmouseover', 'html_event_onmouseup',
    'html_event_onsubmit', 'html_number_keywords_evil', 'js_file', 'js_pseudo_protocol', 'js_dom_location',
    'js_dom_document', 'js_prop_cookie', 'js_prop_referrer', 'js_method_write', 'js_method_getElementsByTagName',
    'js_method_getElementById', 'js_method_alert', 'js_method_eval', 'js_method_fromCharCode', 'js_method_confirm',
    'js_min_length', 'js_min_define_function', 'js_min_function_calls', 'js_string_max_length', 'Label'
]
# Export the decision tree to a .dot file
export_graphviz(model, out_file="tree.dot", feature_names=feature_names, class_names=['0', '1'], filled=True, rounded=True)

# Convert the .dot file to a PDF image with a specified DPI
with open("tree.dot") as f:
    dot_graph = f.read()

# Create the graph object
graph = graphviz.Source(dot_graph)

# Set the size of the graph
graph.size = '8,8'

# Export the graph as a PDF with a specified DPI
graph.render("decision_tree", format="pdf", cleanup=True)

import numpy as np
import matplotlib.pyplot as plt
import chardet
from lime.lime_tabular import LimeTabularExplainer

def predict_fn(X):
    return clf.predict_proba(X)

instance_idx = 0
instance = X_test[instance_idx]

print("Instance shape:", instance.shape)

print("Number of feature names:", len(feature_names))
print("Feature names:", feature_names)

explainer = LimeTabularExplainer(X_train, feature_names=feature_names, class_names=['Not Malicious', 'Malicious'], discretize_continuous=True)
exp = explainer.explain_instance(instance, predict_fn)


print("Explanation as text:")
print(exp.as_list())

print("Plotting explanation...")
exp.show_in_notebook()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import chardet
from lime.lime_tabular import LimeTabularExplainer

def predict_fn(X):
    return clf.predict_proba(X)

instance_idx = 0
instance = X_test[instance_idx]

print("Instance shape:", instance.shape)


print("Number of feature names:", len(feature_names))
print("Feature names:", feature_names)

explainer = LimeTabularExplainer(X_train, feature_names=feature_names, class_names=['Not Malicious', 'Malicious'], discretize_continuous=True)
exp = explainer.explain_instance(instance, predict_fn)


print("Explanation as text:")
print(exp.as_list())


print("Plotting explanation...")
fig = exp.as_pyplot_figure()
plt.show()

fig.savefig("explanation.pdf")