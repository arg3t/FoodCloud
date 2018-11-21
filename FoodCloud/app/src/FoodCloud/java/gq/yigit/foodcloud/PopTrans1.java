package gq.yigit.foodcloud;

import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import static android.support.constraint.Constraints.TAG;

public class PopTrans1 extends Activity {
	public TextView duration;
	public TextView from;
	public TextView to;
	public TextView stop;
	public TextView cond;
	public TextView safe_txt;
	public ImageView safe_img;
	public boolean safe;
	public boolean stop_cond;
	public boolean cond_cond;
	public JSONObject json_trans1;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_pop_trans1);
		duration = (TextView)findViewById(R.id.duration);
		from = (TextView)findViewById(R.id.from);
		safe_txt = (TextView)findViewById(R.id.safe_txt);
		to = (TextView)findViewById(R.id.to);
		stop = (TextView)findViewById(R.id.stop);
		cond = (TextView)findViewById(R.id.cond);		
		safe_img = (ImageView) findViewById(R.id.safe_img);

		Bundle extras = getIntent().getExtras();
		if (extras != null) {
			try {
				json_trans1 = new JSONObject(extras.getString("key"));
				duration.setText(json_trans1.get("Duration").toString() + " hours");
				safe = (boolean)json_trans1.get("Problematic");
				to.setText(json_trans1.get("Moved to,from").toString().split("-")[1]);
				from.setText(json_trans1.get("Moved to,from").toString().split("-")[0]);
				stop_cond = (boolean)json_trans1.get("Stopped");
				cond_cond = (boolean)json_trans1.get("Condition");
			}catch(JSONException e){
				Log.d(TAG,"An error occured with json!");
			}
		}
		if(safe){
			safe_img.setImageResource(R.mipmap.warning);
			safe_txt.setText("Warning, there was an error in the harvestment of this product. We recommend that you don't consume it!");
		}else{
			safe_img.setImageResource(R.mipmap.check);
			safe_txt.setText("This product did not have any problems during harvesting. It is safe to consume!");
		}
		if(stop_cond){
			stop.setText("Yes");
		}else{
			stop.setText("No");
		}
		if(cond_cond){
			cond.setText("Yes");
		}else{
			cond.setText("No");
		}

		DisplayMetrics dm = new DisplayMetrics();
		getWindowManager().getDefaultDisplay().getMetrics(dm);
		int width = dm.widthPixels;
		int height = dm.heightPixels;
		getWindow().setLayout((int)(width*0.8), (int)(height*0.72));
	}
}
