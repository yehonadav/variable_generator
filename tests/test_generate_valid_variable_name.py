import unittest

from variable_generator.name_generator import generate_valid_variable_name, valids


class TestGenerationOfValidVariableNames(unittest.TestCase):
    testing_data = dict(
        string1 = valids,
        string2 = "(*&^%$#@",
        string3 = " ",
        string4 = "  ",
        string5 = "     ",
        string6 = " 123ghb321 ",
        string7 = "   12  GHss *&^T% 1 ",
        string8 = "'''''''",
        string9 = "1",
        string10 = "123",
        string11 = "98asdcv98",
        string12 = " 12asdf gh0987 ",
        string13 = " 12a%^sdf gh0987 ",
        string14 = "",
        string15 = "'slabiky, ale liší se podle významu'",
        string16 = "English",
        string17 = "ގެ ފުރަތަމަ ދެ އަކުރު ކަ",
        string18 = "how about this one : 通 asfަ",
        string19 = "?fd4))45s&",
        string20 = "Текст на русском",
        string21 = "וּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵ",
        string22 = "וּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵ",
        string23 = 10,
    )

    # expected results
    expected_results = (
        valids,
        "round_left_bracket_asterisk_ampersand_circumflex_percent_dollar_pound_at_sign",
        (ValueError, "string cannot have only spaces"),
        "num123ghb321",
        "num12_GHss_asterisk_ampersand_circumflex_T_percent_1",
        "quotation_mark_quotation_mark_quotation_mark_quotation_mark_quotation_mark_quotation_mark_quotation_mark",
        "num1",
        "num123",
        "num98asdcv98",
        "num12asdf_gh0987",
        "num12a_percent_circumflex_sdf_gh0987",
        (ValueError, "empty string"),
        "quotation_mark_slabiky_comma_ale_li353237_se_podle_v253znamu_quotation_mark",
        "English",
        "num19341964_19301962192319581932195819291958_19311964_192719581926196219231962_19261958",
        "how_about_this_one_colon_36890_asf1958",
        "question_mark_fd4_round_right_bracket_round_right_bracket_45s_ampersand",
        "num10581077108210891090_10851072_1088109110891089108210861084",
        "num14931468_1493146414891465149214931468_comma_149314561495146515131473146214981456_comma_150614631500_hyphen_minus_15081468145615041461",
        TypeError
    )

    def test_generate_valid_variable_name(self):

        with self.assertRaises(self.expected_results[2][0], msg=self.expected_results[2][1]):
            generate_valid_variable_name(self.testing_data['string3'])
        with self.assertRaises(self.expected_results[2][0], msg=self.expected_results[2][1]):
            generate_valid_variable_name(self.testing_data['string4'])
        with self.assertRaises(self.expected_results[2][0], msg=self.expected_results[2][1]):
            generate_valid_variable_name(self.testing_data['string5'])
        with self.assertRaises(self.expected_results[11][0], msg=self.expected_results[11][1]):
            generate_valid_variable_name(self.testing_data['string14'])
        with self.assertRaises(self.expected_results[19]):
            generate_valid_variable_name(self.testing_data['string23'])

        self.assertEqual(generate_valid_variable_name(self.testing_data['string1']), self.expected_results[0])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string2']), self.expected_results[1])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string6']), self.expected_results[3])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string7']), self.expected_results[4])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string8']), self.expected_results[5])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string9']), self.expected_results[6])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string10']), self.expected_results[7])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string11']), self.expected_results[8])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string12']), self.expected_results[9])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string13']), self.expected_results[10])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string15']), self.expected_results[12])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string16']), self.expected_results[13])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string17']), self.expected_results[14])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string18']), self.expected_results[15])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string19']), self.expected_results[16])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string20']), self.expected_results[17])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string21']), self.expected_results[18])
        self.assertEqual(generate_valid_variable_name(self.testing_data['string22']), self.expected_results[18])


if __name__ == '__main__':
    unittest.main()
