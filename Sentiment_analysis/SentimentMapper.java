import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class SentimentMapper extends Mapper<Object, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text sentiment = new Text();

    // Define some simple positive and negative words (you can expand this list)
    private static final String[] positiveWords = {"good", "happy", "love", "great", "excellent", "awesome"};
    private static final String[] negativeWords = {"bad", "sad", "hate", "terrible", "awful", "horrible"};

    // Mapper logic to classify sentiment
    @Override
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String text = value.toString().toLowerCase();
        int positiveCount = 0;
        int negativeCount = 0;

        // Check if any positive words exist in the text
        for (String word : positiveWords) {
            if (text.contains(word)) {
                positiveCount++;
            }
        }

        // Check if any negative words exist in the text
        for (String word : negativeWords) {
            if (text.contains(word)) {
                negativeCount++;
            }
        }

        // Determine sentiment based on the counts
        if (positiveCount > negativeCount) {
            sentiment.set("Positive");
        } else if (negativeCount > positiveCount) {
            sentiment.set("Negative");
        } else {
            sentiment.set("Neutral");
        }

        // Emit the sentiment and count (1)
        context.write(sentiment, one);
    }
}
