no = ["ab", "ad", "be", "dg", "fi", "ac", "ap", "cs", "ae", "be", "af", "am", "bn", "ag", "ci", "ah", "aj", "bk", "ar", "at", "bu", 
"ia", "ib", "ic", "id", "ie", "if", "ig", "ih", "ka", "kb", "kc", "kd", "ke", "kf", "kg", "kh", "la", "lb", "lc", "ld", "le", "lf", "lg", "lh", 
"na", "nb", "nc", "nd", "ne", "nf", "ng", "nh", "oa", "ob", "oc", "od", "oe", "of", "og", "oh", "sa", "sb", "sc", "sd", "se", "sf", "sg", "sh",
"va", "vb", "vc", "vd", "ve", "vf", "vg", "vh", "bc", "dp", "bd", "dm", "bf", "bg", "bh", "dj", "bj", "bp", "br", "dt", "cd", "nr", "pm", "cg", 
"ch", "rj", "kr", "cj", "cp", "cr", "pt", "ru", "ct", "de", "df", "eh", "gj", "hk", "dj", "dh", "dr", "ef", "gm", "eg", "ej", "ep", "er", "gt", 
"hu", "et", "gf", "fj", "fp", "ft", "gh", "gr", "hj", "hp", "pj", "ht", "pr", "rt", "bm", "cm", "em", "hm"]

yes = ["ce", "pg", "is", "il", "iv", "io", "ik", "in", "iu",   "sl", "sv", "so", "sk", "sn", "su"  "lv", "lo", "lk", "ln", "lu",  "vo", "vk", "vn", "vu"   
"fh", "fr",  "hr",   "kn", "ku",  "nu",    "tj", "tm",  "jm"]

def reverse(str):
	out = ""
	for i in str:
		out = i + out

	return out


def fun(str):
	rev = reverse(str)
	for i in no:
		if (i == str or i == rev):
			return "cannot be"
	for i in yes:
		if (i == str or i == rev):
					return "it is"

	return "cant say"

str = input("write: ")

print(fun(str))