
# convert dna sequence string csv file to dna label encoder csv file
from class_convert_dna_label_encoder import ConvertDNALabelEncoder
dna_string_csv_path = r"\folder_path\dna_sequence_string_example.csv"
dna_labelencoder_csv_path = r"\folder_path\dna_label_encoder_example.csv"
ConvertDNALabelEncoder.convert_dna_string_to_dna_labelencoder(dna_string_csv_path, dna_labelencode_csv_path)

# convert dna label encoder csv file to dna sequence string csv file
from class_convert_dna_label_encoder import ConvertDNALabelEncoder
dna_string_csv_path_back = r"\folder_path\dna_sequence_string_example_back.csv"
dna_labelencoder_csv_path = r"\folder_path\dna_label_encoder_example.csv"
ConvertDNALabelEncoder. convert_dna_labelencoder_to_dna_string(dna_string_csv_path_back, dna_labelencode_csv_path)
