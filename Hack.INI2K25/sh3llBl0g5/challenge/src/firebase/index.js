import {
  initializeApp
} from "firebase/app";
import {
  collection,
  getFirestore,
  query,
  orderBy
} from "firebase/firestore";
import {
  getAuth
} from "firebase/auth";
import {
  getStorage
} from "firebase/storage";

const firebaseConfig = {
  apiKey: process.env.VUE_APP_AKEY,
  authDomain: process.env.VUE_APP_ADOMAIN,
  projectId: process.env.VUE_APP_PID,
  storageBucket: process.env.VUE_APP_SBUCKET,
  messagingSenderId: process.env.VUE_APP_MSID,
  appId: process.env.VUE_APP_AID
};

initializeApp(firebaseConfig);

const auth = getAuth();

const storage = getStorage();

const db = getFirestore();

const colRef = collection(db, 'bXl1c2Vyc2xpc3Q');

const blogsRef = collection(db, 'bXlibG9nc2xpc3Q');

const THERef = collection(db, 'bG9ncw');

const newBlogsRef = query(blogsRef, orderBy("blogTime", "desc"));

export {
  auth,
  storage,
  db,
  colRef,
  blogsRef,
  newBlogsRef,
  THERef
}