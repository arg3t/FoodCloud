package gq.yigit.foodcloud;

import android.app.Activity;
import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import static android.support.constraint.Constraints.TAG;

public class PackagePop extends Activity {
	public TextView material;
	public TextView location;
	public TextView cancerogen;
	public ImageView safe_img;
	public TextView safe_txt;
	public boolean cancerogens;
	public boolean safe;
	public JSONObject json_pack;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_package_pop);
		safe_txt = (TextView)findViewById(R.id.safe_txt);
		material = (TextView)findViewById(R.id.material);
		location = (TextView)findViewById(R.id.place);
		cancerogen = (TextView)findViewById(R.id.cancerogen);
		safe_img = (ImageView) findViewById(R.id.safe_img);
		Bundle extras = getIntent().getExtras();
		if (extras != null) {
			try {
				json_pack = new JSONObject(extras.getString("key"));
				location.setText((String)json_pack.get("Location"));
				safe = (boolean)json_pack.get("Problematic");
				material.setText(json_pack.get("Material").toString());
				cancerogens = (boolean) json_pack.get("Cancerogen");
			}catch(JSONException e){
				Log.d(TAG,"An error occured with json!");
			}
		}
		if(cancerogens){
			cancerogen.setText("Yes");
		}else{
			cancerogen.setText("No");
		}
		if(safe){
			safe_img.setImageResource(R.mipmap.warning);
			safe_txt.setText("Warning, there was an error in the packaging of this product. We recommend that you don't consume it!");
		}else{
			safe_img.setImageResource(R.mipmap.check);
			safe_txt.setText("This product did not have any problems during packaging. It is safe to consume!");
		}


		DisplayMetrics dm = new DisplayMetrics();
		getWindowManager().getDefaultDisplay().getMetrics(dm);
		int width = dm.widthPixels;
		int height = dm.heightPixels;
		getWindow().setLayout((int)(width*0.821), (int)(height*0.5));
	}
}
