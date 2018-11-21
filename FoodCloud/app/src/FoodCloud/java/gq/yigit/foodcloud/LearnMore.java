/*
PAUSE FOR PRAYER

Dear God,
Please help me find any malicious bugs that I've created
and ,yet, I can't spot.
Make my code free of errors.


END PRAYER
*/

package gq.yigit.foodcloud;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LearnMore extends AppCompatActivity implements View.OnClickListener {
    private static final String TAG = "MainActivity";
    public String prod_loc_more;
    public ImageView factory;
    public ImageView farm;
    public ImageView packaging;
    public ImageView trans1;
    public ImageView trans2;
    static public ImageView factory_cond;
    static public ImageView farm_cond;
    static public ImageView packaging_cond;
    static public ImageView trans1_cond;
    static public ImageView trans2_cond;

    public Button back_to_main;
    public Map<String, Object> someMap;
    public String prod_loc;
    static public JSONObject process;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        System.gc();
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            prod_loc_more = extras.getString("key");
        }
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_learn_more);
        factory = (ImageView) findViewById(R.id.factory);
        factory_cond = (ImageView) findViewById(R.id.factory_cond);
        factory.setOnClickListener(this);
        farm = (ImageView) findViewById(R.id.farm);
        farm_cond = (ImageView) findViewById(R.id.farm_cond);
        farm.setOnClickListener(this);
        packaging = (ImageView) findViewById(R.id.packaging);
        packaging_cond = (ImageView) findViewById(R.id.packaging_cond);
        packaging.setOnClickListener(this);
        trans1 = (ImageView) findViewById(R.id.trans1);
        trans1_cond = (ImageView) findViewById(R.id.trans1_cond);
        trans1.setOnClickListener(this);
        trans2 = (ImageView) findViewById(R.id.trans2);
        trans2_cond = (ImageView) findViewById(R.id.trans2_cond);
        trans2.setOnClickListener(this);
        back_to_main = (Button) findViewById(R.id.go_back_to_main);
        back_to_main.setOnClickListener(this);
        PHPComm comm = new PHPComm(this);
        PHPComm.decide = "Proc";
        comm.execute("get", prod_loc_more, "Processes");

    }

    public void onClick(View v){
        try {
            if (v.getId() == R.id.go_back_to_main) {
                Intent i = new Intent(LearnMore.this, MainActivity.class);
                startActivity(i);
            } else if (v.getId() == R.id.factory) {
                Intent i = new Intent(LearnMore.this, ProcessPop.class);
                i.putExtra("key", process.get("Process").toString());
                startActivity(i);
            } else if (v.getId() == R.id.farm) {
                Intent i = new Intent(LearnMore.this, FarmPop.class);
                i.putExtra("key", process.get("Harvested").toString());
                startActivity(i);
            } else if (v.getId() == R.id.packaging) {
                Intent i = new Intent(LearnMore.this, PackagePop.class);
                i.putExtra("key", process.get("Packaging").toString());
                startActivity(i);
            } else if (v.getId() == R.id.trans1) {
                Intent i = new Intent(LearnMore.this, PopTrans1.class);
                i.putExtra("key", process.get("Transport1").toString());
                startActivity(i);
            } else if (v.getId() == R.id.trans2) {
                Intent i = new Intent(LearnMore.this, PopTrans2.class);
                i.putExtra("key", process.get("Transport2").toString());
                startActivity(i);
            }
        }catch(JSONException e){
            Log.d(TAG,"An error occured with json");
        }
    }
    static public void adjustImg(ImageView comp,String stage) {
        try {
            if ((boolean) process.getJSONObject(stage).get("Problematic")) {
                comp.setImageResource(R.mipmap.warning);
                comp.bringToFront();
            } else {
                comp.setImageResource(R.mipmap.check);
                comp.bringToFront();
            }
        } catch (JSONException e) {
            Log.d(TAG, "An error ocuured with the json");
        }
    }
        
    static public void continueProg(String result){
        try {
            process = new JSONObject(result);
        }catch (JSONException e){
            Log.d(TAG,"An error ocuured with the json");
        }
        Log.d(TAG,"Received JSON: " + process.toString());
        adjustImg(factory_cond,"Process");
        adjustImg(farm_cond,"Harvested");
        adjustImg(packaging_cond,"Packaging");
        adjustImg(trans1_cond,"Transport1");
        adjustImg(trans2_cond,"Transport2");
    }
}
