import React from 'react';
import Toast,{ErrorToast, InfoToast, SuccessToast} from 'react-native-toast-message';

export const showToast = (type, text1, text2) => {
  Toast.show({
    type: type,
    position: "top",
    text1: text1,
    text2: text2,
    visibilityTime: 5000,
    autoHide: true,
    topOffset: 100,
    bottomOffset: 40,
  });
};

export const toastConfig = {
  /* 
    overwrite 'success' type, 
    modifying the existing `BaseToast` component
  */
  info: ({text1, text2, props, ...rest}) => (
    <InfoToast
      {...rest}
      contentContainerStyle={{paddingHorizontal: 15}}
      text1Style={{
        fontSize: 17,
        fontWeight: 'bold',
      }}
      text2Style={{
        fontSize: 12,
      }}
      text1={text1}
      text2={text2}
      leadingIcon={props.info}
    />
  ),
  success: ({text1, text2, props, ...rest}) => (
    <SuccessToast
      {...rest}
      contentContainerStyle={{paddingHorizontal: 15}}
      text1Style={{
        fontSize: 20,
        fontWeight: '900',
      }}
      text2Style={{
        fontSize: 12,
        fontWeight: '700',
      }}
      text1={text1}
      text2={text2}
    />
  ),
  /*
    Reuse the default ErrorToast toast component
  */
  error: props => (
    <ErrorToast
      {...props}
      text1Style={{
        fontSize: 17,
        fontWeight: '900',
      }}
      text2Style={{
        fontSize: 15,
      }}
    />
  ),
};
