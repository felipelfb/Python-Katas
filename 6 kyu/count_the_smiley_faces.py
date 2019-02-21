# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :] 

# Example cases:

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

# Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same

# https://www.codewars.com/kata/count-the-smiley-faces

def count_smileys(arr):
    smiley_faces_count = 0
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    if len(arr) == 0:
        return 0
    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouth:
                smiley_faces_count += 1
        if len(face) == 3:
            if face[0] in eyes and face[1] in nose and face[2] in mouth:
                smiley_faces_count += 1
    return smiley_faces_count