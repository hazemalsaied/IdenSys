class ToCSVFile:
    @staticmethod
    def toCSVFile(textFilePath):
        """
            export the output of Talismane into CSV file
            :param textFilePath: the path of textual input file.
            :return: CSV file of Talismane output
        """
        result = 'ID,FORM,LEMMA,UPOSTAG,XPOSTAG,FEATS,HEAD,DEPREL,DEPS,MISC\n'
        ff = open(textFilePath, 'r')
        lines = ff.readlines()
        for line in lines:
            parts = line.split('\t')
            for part in parts:
                if part.strip() == ',':
                    part = 'COMMA'
                result += part.strip() + ','
            result = result[:-1] + '\n'
        pathParts = textFilePath.split('/')
        ff.close()
        # Writing to ouptput file
        outputPath = '/'
        for pathPart in pathParts[:len(pathParts) - 1]:
            outputPath += pathPart + '/'
        outputPath += 'output.csv'
        outputFile = open(outputPath, 'w+')
        outputFile.write(result)
        outputFile.close()


inputFile = '/Users/hazemalsaied/Documents/result.txt'
ToCSVFile.toCSVFile(inputFile)