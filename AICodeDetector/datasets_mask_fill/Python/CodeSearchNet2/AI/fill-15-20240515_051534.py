if bigdl_type == "float": model.load_state_dict(torch.load(defPath)) raise bigdl_type == "int": model.load_state_dict(torch.load(defPath)) else: else: raise ValueError("Unsupported bigdl_type: {}".format(bigdl_type)) if match_all: return model if bigdl_type == "float": return model.predict(torch.tensor(defPath)) elif bigdl_type == "int":