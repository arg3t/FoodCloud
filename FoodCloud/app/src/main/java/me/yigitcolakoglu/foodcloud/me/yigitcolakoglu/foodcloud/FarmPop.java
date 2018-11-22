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

public class FarmPop extends Activity {


	public JSONObject json_farm;
	public TextView date;
	public TextView place;
	public TextView prod;
	public TextView safe_txt;
	public ImageView safe_img;
	public boolean proc_safe;
	private static final String TAG = "MainActivity";
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_farm_pop);
		place = (TextView)findViewById(R.id.loc);
		date = (TextView)findViewById(R.id.Date);
		safe_txt = (TextView)findViewById(R.id.safe_txt);
		prod = (TextView)findViewById(R.id.prod);
		safe_img = (ImageView) findViewById(R.id.safe_img);
		Bundle extras = getIntent().getExtras();
		if (extras != null) {
			try {
				json_farm = new JSONObject(extras.getString("key"));
				place.setText((String)json_farm.get("Location"));
				proc_safe = (boolean)json_farm.get("Problematic");
				date.setText(json_farm.get("Date").toString());
				prod.setText((json_farm.get("Product").toString()));
			}catch(JSONException e){
				Log.d(TAG,"An error occured with json!");
			}
		}
		if(proc_safe){
			safe_img.setImageResource(R.mipmap.warning);
			safe_txt.setText("Warning, there was an error in the harvestment of this product. We recommend that you don't consume it!");
		}else{
			safe_img.setImageResource(R.mipmap.check);
			safe_txt.setText("This product did not have any problems during harvesting. It is safe to consume!");
		}

		DisplayMetrics dm = new DisplayMetrics();
		getWindowManager().getDefaultDisplay().getMetrics(dm);
		int width = dm.widthPixels;
		int height = dm.heightPixels;
		getWindow().setLayout((int)(width*0.8), (int)(height*0.55));
	}
}
